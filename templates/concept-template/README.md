# Concept Template (Language-Agnostic)

Use this template when creating a new concept module in any track.
All section headings below are required by repository validation scripts, including `Learning Metadata`.

When writing `example/main.*`, start with a short header comment that states the module focus and why it matters, then add intent-first comments before meaningful logic blocks so new developers can follow program flow quickly.

## Learning Metadata

- Difficulty:
- Estimated Time:
- Prerequisites:
- Cross-Language Lens:

## Quick Run

Include one command that runs the module example.

~~~bash
# C++
g++ -std=c++17 -Wall -Wextra -pedantic example/main.cpp -o concept_example
./concept_example

# Python
python example/main.py

# Go
go run example/main.go

# Java
javac -d build/java example/Main.java
java -cp build/java Main

# C#
dotnet run --project example/concept-template-example.csproj

# TypeScript
npm run build:typescript
node build/typescript/<level>/<module>/example/main.js
~~~

## Topics Covered

- Topic 1
- Topic 2
- Topic 3

## Common Pitfalls

- Pitfall 1
- Pitfall 2

## Cross-Language Notes

- Comparison point 1
- Comparison point 2
- Comparison point 3

## Exercise Focus

- exercises/01.<ext> or Exercise01.java: short task summary.
- exercises/02.<ext> or Exercise02.java: short task summary.

### Exercise Specs

1. exercises/01.<ext> or Exercise01.java
- Input:
- Output:
- Edge cases:

2. exercises/02.<ext> or Exercise02.java
- Input:
- Output:
- Edge cases:

## Checkpoint

- [ ] I understand the core ideas of this module.
- [ ] I can run and explain the example.
- [ ] I completed exercise 01.
- [ ] I completed exercise 02.
