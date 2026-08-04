from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.automation_core.manifest import Manifest
from scripts.automation_core.ops import RepoContext, compile_java_source


class JavaAutomationTests(unittest.TestCase):
    @patch("scripts.automation_core.ops.run_command")
    @patch("scripts.automation_core.ops.find_java_tool", return_value="javac")
    def test_compiler_can_discover_sibling_sources(self, _find_java, run_command) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source_dir = root / "example"
            source_dir.mkdir()
            source_path = source_dir / "Main.java"
            source_path.write_text("public class Main {}\n", encoding="utf-8")
            output_dir = root / "classes"
            ctx = RepoContext(root=root, scripts_dir=root / "scripts", manifest=Manifest({}))

            compile_java_source(ctx, source_path, output_dir)

        command = run_command.call_args.args[0]
        self.assertEqual(command[0], "javac")
        self.assertEqual(command[command.index("-sourcepath") + 1], str(source_dir))
        self.assertEqual(command[-1], str(source_path))


if __name__ == "__main__":
    unittest.main()
