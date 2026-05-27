import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        Path inputPath = Path.of(scanner.nextLine().trim());
        Path outputPath = Path.of(scanner.nextLine().trim());

        List<String> inputLines = Files.readAllLines(inputPath);
        List<String> outputLines = new ArrayList<>();
        for (int i = 0; i < inputLines.size(); i++) {
            outputLines.add((i + 1) + ": " + inputLines.get(i));
        }

        Files.write(outputPath, outputLines);
        System.out.println("Lines copied: " + inputLines.size());
    }
}
