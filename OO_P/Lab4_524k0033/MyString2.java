package Lab4_524k0033;

import java.util.Scanner;

public class MyString2 {
	
    public static int countWord(String paragraph) {
        if (paragraph == null || paragraph.trim().isEmpty()) {
            return 0;
        }
        String[] words = paragraph.trim().split("\\s+");
        return words.length;
    }

    public static int countSentences(String paragraph) {
        if (paragraph == null || paragraph.trim().isEmpty()) {
            return 0;
        }
        String[] sentences = paragraph.split("[.!?]+");
        return sentences.length;
    }

    public static int countAppear(String paragraph, String word) {
        if (paragraph == null || paragraph.trim().isEmpty() || word == null || word.trim().isEmpty()) {
            return 0;
        }
        int count = 0;
        String[] words = paragraph.toLowerCase().split("\\s+");
        String targetWord = word.toLowerCase();
        for (String w : words) {
            
            String cleanedWord = w.replaceAll("[^a-zA-Z0-9]", "");
            if (cleanedWord.equals(targetWord)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String paragraph = "The Edge Surf is of course also a whole lot better, which will hopefully win Microsoft some converts. It offers time trial, support for other input methods like touch and gamepads, accessibility improvements, high scores, and remastered visuals.";

        System.out.println("Word count: " + countWord(paragraph));
        System.out.println("Sentence count: " + countSentences(paragraph));
		System.out.print("Enter a word :");
		Scanner in = new Scanner(System.in);
		String word=in.nextLine();
        System.out.printf("Occurrences of %s: %d",word,countAppear(paragraph,word));
		in.close();

    }
}

