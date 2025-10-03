import java.util.Scanner;

public class DictionaryManagement {

    private static String[][] dictionary = new String[100][11]; // [word][10 meanings + word]
    private static int wordCount = 0;

    public static void addWord(String word, String meaning) {
        int wordIndex = findWordIndex(word);
        if (wordIndex == -1) { // New word
            if (wordCount < 100) {
                dictionary[wordCount][0] = word;
                dictionary[wordCount][1] = meaning;
                wordCount++;
                System.out.println("Word/meaning added successfully.");
            } else {
                System.out.println("Dictionary is full.");
            }
        } else { // Existing word
            int meaningCount = 0;
            for (int i = 1; i < 11; i++) {
                if (dictionary[wordIndex][i] != null) {
                    meaningCount++;
                }
            }
            if (meaningCount < 10) {
                boolean duplicate = false;
                for(int i = 1; i < 11; i++){
                    if(meaning.equals(dictionary[wordIndex][i])){
                        duplicate = true;
                        break;
                    }
                }
                if(!duplicate){
                    dictionary[wordIndex][meaningCount + 1] = meaning;
                    System.out.println("Word/meaning added successfully.");
                } else{
                    System.out.println("Meaning already exists.");
                }

            } else {
                System.out.println("Maximum meanings reached for this word.");
            }
        }
    }

    public static void removeMeaning(String word, int meaningIndex) {
        int wordIndex = findWordIndex(word);
        if (wordIndex != -1) {
            if (dictionary[wordIndex][meaningIndex + 1] != null) {
                for (int i = meaningIndex + 1; i < 10; i++) {
                    dictionary[wordIndex][i] = dictionary[wordIndex][i + 1];
                }
                dictionary[wordIndex][10] = null; // Clear last element
                System.out.println("Meaning removed successfully.");
            } else {
                System.out.println("Meaning index not found.");
            }
        } else {
            System.out.println("Word not found.");
        }
    }

    public static void lookUpWord(String word) {
        int wordIndex = findWordIndex(word);
        if (wordIndex != -1) {
            System.out.println("Word: " + dictionary[wordIndex][0]);
            System.out.println("Meanings:");
            int meaningCount = 0;
            for (int i = 1; i < 11; i++) {
                if (dictionary[wordIndex][i] != null) {
                    System.out.println(meaningCount + ") " + dictionary[wordIndex][i]);
                    meaningCount++;
                }
            }
        } else {
            System.out.println("Word not found.");
        }
    }

    public static int getWordCount() {
        return wordCount;
    }

    private static int findWordIndex(String word) {
        for (int i = 0; i < wordCount; i++) {
            if (dictionary[i][0] != null && dictionary[i][0].equals(word)) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n1. Add Word (or Add Meaning to Existing Word)");
            System.out.println("2. Remove Meaning");
            System.out.println("3. Look Up Word");
            System.out.println("4. Check Word Count");
            System.out.println("5. Exit");
            System.out.print("Select an option: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter word: ");
                    String word = scanner.nextLine();
                    System.out.print("Enter meaning: ");
                    String meaning = scanner.nextLine();
                    addWord(word, meaning);
                    break;
                case 2:
                    System.out.print("Enter word: ");
                    word = scanner.nextLine();
                    lookUpWord(word);
                    System.out.print("Enter index of meaning to remove: ");
                    int meaningIndex = scanner.nextInt();
                    removeMeaning(word, meaningIndex);
                    scanner.nextLine();
                    break;
                case 3:
                    System.out.print("Enter word to look up: ");
                    word = scanner.nextLine();
                    lookUpWord(word);
                    break;
                case 4:
                    System.out.println("Total words in dictionary: " + getWordCount());
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option.");
            }
        } while (choice != 5);

        scanner.close();
    }
}