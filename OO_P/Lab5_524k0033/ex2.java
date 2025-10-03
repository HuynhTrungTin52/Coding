package Lab5_524k0033;

public class ex2 {

    public static void main(String[] args) {
        String paragraph = "You are living on a Plane. What you style Flatland is the vast level surface of what I may call a fluid, on, or in, the top of which you and your countrymen move about, without rising above it or falling below it.";
        String[] words = paragraph.toLowerCase().split("[\s.,]+"); // Split into words, lowercase, remove punctuation

        String[][] wordFrequency = new String[words.length][2]; // Max size, will trim later
        int wordCount = 0;

        for (String word : words) {
            boolean found = false;
            for (int i = 0; i < wordCount; i++) {
                if (wordFrequency[i][0].equals(word)) {
                    int frequency = Integer.parseInt(wordFrequency[i][1]);
                    wordFrequency[i][1] = String.valueOf(frequency + 1);
                    found = true;
                    break;
                }
            }
            if (!found) {
                wordFrequency[wordCount][0] = word;
                wordFrequency[wordCount][1] = "1";
                wordCount++;
            }
        }

        // Trim the array to the actual number of unique words
        String[][] result = new String[wordCount][2];
        for (int i = 0; i < wordCount; i++) {
            result[i][0] = wordFrequency[i][0];
            result[i][1] = wordFrequency[i][1];
        }

        // Print the result
        for (String[] row : result) {
            System.out.println("'" + row[0] + "': " + row[1] + ",");
        }
    }
}