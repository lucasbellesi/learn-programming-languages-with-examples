# C++ Setup (VS Code + g++)

This setup supports:

- Windows with MSYS2 + MinGW g++
- Linux with g++

## Verify Compiler

Run:

```bash
g++ --version
```

You should see an installed GNU C++ compiler.

## Compile Command (C++17)

```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp -o main
```

## Run

Linux:

```bash
./main
```

Windows (MSYS2 shell):

```bash
./main.exe
```

## VS Code Notes

- Recommended extensions are in `.vscode/extensions.json`.
- C++ standard is set to C++17 in `.vscode/settings.json`.
- Build task compiles the currently open C++ file in place.
