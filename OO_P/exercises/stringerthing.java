package exercises;

import java.util.*;

public class stringerthing {

	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {

			System.out.print("Please enter your name :");
			String name = in.nextLine();
			StringTokenizer nameToken = new StringTokenizer(name, " ");
			int words = nameToken.countTokens();
			int words2 = 0;
			@SuppressWarnings("ReplaceStringBufferByString")
			StringBuffer firstName = new StringBuffer("");
			@SuppressWarnings("ReplaceStringBufferByString")
			StringBuilder middleName = new StringBuilder("");
			@SuppressWarnings("ReplaceStringBufferByString")
			StringBuffer lastName = new StringBuffer("");
			StringBuilder properName = new StringBuilder("");
			while (nameToken.hasMoreTokens()) {
				if (words2 == 0) {
					
					firstName.append(nameToken.nextToken());
					firstName.replace(0, 1, firstName.substring(0, 1).toUpperCase());
				}
				if (words2 != 0 && words2 != words-1) {
					StringBuilder tempStr = new StringBuilder("");
					tempStr.append(nameToken.nextToken());
					tempStr.replace(0,1,tempStr.substring(0,1).toUpperCase());
					middleName.append(tempStr).append(" ");
				}
				if (words2 == words-1) {
					lastName.append(nameToken.nextToken());
					lastName.replace(0,1,lastName.substring(0,1).toUpperCase());
				}
				words2++;
			}
			properName.append(firstName).append(" ").append(middleName).append(lastName);
			System.out.println("The number of words is :" + words);
			System.out.println("The first name is :" + firstName);
			System.out.println("The middle name is :" + middleName);
			System.out.println("The last name is :"+lastName);
			System.out.print("Full name :"+properName);
		}

	}
}