package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Input file path: ")
	inputPath, _ := reader.ReadString('\n')
	inputPath = strings.TrimSpace(inputPath)

	fmt.Print("Output file path: ")
	outputPath, _ := reader.ReadString('\n')
	outputPath = strings.TrimSpace(outputPath)

	if inputPath == "" || outputPath == "" {
		fmt.Println("Both paths are required.")
		return
	}

	inputFile, err := os.Open(inputPath)
	if err != nil {
		fmt.Println("Could not open input file.")
		return
	}
	defer inputFile.Close()

	outputFile, err := os.Create(outputPath)
	if err != nil {
		fmt.Println("Could not create output file.")
		return
	}
	defer outputFile.Close()

	scanner := bufio.NewScanner(inputFile)
	lineNumber := 1
	for scanner.Scan() {
		fmt.Fprintf(outputFile, "%d: %s\n", lineNumber, scanner.Text())
		lineNumber++
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("File processing failed.")
		return
	}

	fmt.Printf("Copied %d lines.\n", lineNumber-1)
}
