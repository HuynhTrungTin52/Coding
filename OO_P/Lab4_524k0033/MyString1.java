package Lab4_524k0033;

public class MyString1 {
	public static String shortName(String str) {
        if (str == null || str.trim().isEmpty()) {
            return "";
        }

        String[] names = str.trim().split("\\s+");
        if (names.length < 2) {
            return str; // If only one name, return as is.
        }

        return names[names.length - 1] + " " + names[0];
    }

	public static String hashtagName(String str) {
        if (str == null || str.trim().isEmpty()) {
            return "#";
        }
        String[] names = str.trim().split("\\s+");
        if (names.length < 2) {
            return "#"+ str;
        }

        return "#" + names[names.length - 1] + names[0];
    }

    public static String upperCaseAllVowel(String str) {
        if (str == null) {
            return null;
        }
        StringBuilder result = new StringBuilder();
        for (char c : str.toCharArray()) {
            if ("aeiouAEIOU".indexOf(c) != -1) {
                result.append(Character.toUpperCase(c));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }

    public static String upperCaseAllN(String str) {
        if (str == null) {
            return null;
        }
        StringBuilder result = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c == 'n' || c == 'N') {
                result.append(Character.toUpperCase(c));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String name = "Nguyen Le Trong Tin";

        System.out.println("Short Name: " + shortName(name));
        System.out.println("Hashtag Name: " + hashtagName(name));
        System.out.println("Uppercase Vowels: " + upperCaseAllVowel(name));
        System.out.println("Uppercase N's: " + upperCaseAllN(name));

        String name2 = "John Doe";
        System.out.println("\nShort Name: " + shortName(name2));
        System.out.println("Hashtag Name: " + hashtagName(name2));
        System.out.println("Uppercase Vowels: " + upperCaseAllVowel(name2));
        System.out.println("Uppercase N's: " + upperCaseAllN(name2));

        String name3 = "SingleName";
        System.out.println("\nShort Name: " + shortName(name3));
        System.out.println("Hashtag Name: " + hashtagName(name3));
        System.out.println("Uppercase Vowels: " + upperCaseAllVowel(name3));
        System.out.println("Uppercase N's: " + upperCaseAllN(name3));
    }
}
