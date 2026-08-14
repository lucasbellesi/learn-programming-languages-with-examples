import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String sentence = scanner.nextLine().trim();
        String[] words = sentence.isEmpty() ? new String[0] : sentence.split("\s+");
        int nonSpaceCharacters = sentence.replace(" ", "").length();
        System.out.println("Words: " + words.length);
        System.out.println("Non-space characters: " + nonSpaceCharacters);
    }
}
