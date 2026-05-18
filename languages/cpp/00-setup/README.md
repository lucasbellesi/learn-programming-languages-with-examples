# C++ Setup (VS Code + g++)

This setup supports:

- Windows with MSYS2 + MinGW g++
- Linux with g++

## Setup Goals

- Install or confirm a C++17-capable `g++` toolchain.
- Compile one small program with the same warning flags used throughout this track.
- Run the compiled program from the terminal.
- Confirm VS Code can build and run the currently open C++ file.

## Verify Compiler

Run:

```bash
g++ --version
```

You should see an installed GNU C++ compiler.

## Install Notes

### Windows (MSYS2 + MinGW)

Use the MSYS2 MinGW shell and install toolchain packages:

```bash
pacman -S --needed mingw-w64-ucrt-x86_64-gcc
```

Then verify:

```bash
g++ --version
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install g++
g++ --version
```

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
- Run task executes the compiled binary from the same folder.
- Combined task builds and runs for faster exercise iteration.

## Build All Examples and Exercises

From the repository root:

PowerShell:

```powershell
./scripts/build-all.ps1
```

Bash:

```bash
bash ./scripts/build-all.sh
```

## Ready When

- [ ] `g++ --version` prints an installed compiler.
- [ ] You can compile with `-std=c++17 -Wall -Wextra -pedantic`.
- [ ] You can run the generated binary from your terminal.
- [ ] VS Code uses the recommended extensions and tasks for build/run loops.
- [ ] `build-all` starts successfully from the repository root.

After setup is working, continue with [01-foundations](../01-foundations/README.md).
