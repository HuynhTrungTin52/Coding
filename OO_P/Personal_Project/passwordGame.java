package Personal_Project;

import java.util.Scanner;

public class passwordGame {

	public static boolean numInStr(String str) {
		for(char c : str.toCharArray()) {
			if(Character.isDigit(c)) {
				return true;
			}
		}
	return false;
	}
	public static boolean above5Let(String str) {
		return str.length()>5;
	}
	public static boolean uppercaseInStr(String str) {
		for(char c : str.toCharArray()) {
			if(Character.isUpperCase(c)) {
				return true;
			}
		}
	return false;
	}
	public static boolean specAtEnd(String str) {
		return (Character.isAlphabetic(str.charAt(str.length()-1)) || Character.isDigit(str.charAt(str.length()-1))) ;	
	}
	
	
	public static int problemNum(String str) {
		if(!numInStr(str)) {
			return 1;
		}
		if(!above5Let(str)) {
			return 2;
		}
		if(!uppercaseInStr(str)) {
			return 3;
		}
		if(specAtEnd(str)) {
			return 4;
		}
	return 0;
	}
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String password;
		boolean retry=true;
		int problem;
		while(retry) {
		System.out.print("Enter password :");
		password = in.nextLine();
		problem=problemNum(password);
		switch (problem) {
			case 1 -> {
				System.out.println("Error 1, the password must have a number");
			}
			case 2 -> {
				System.out.println("Error 2, the password must be above 5 letters");
			}
			case 3 ->{
				System.out.println("Error 3, the password must include an uppercase character");
			}
			case 4 ->{
				System.out.println("Error 4, the password must include a special character at the end");
			}
			case 5 -> {
				System.out.println("Error 5, the passsword ");
			}
			default -> {
				retry=false;
			}
		}
		}
		System.out.print("Password accepted !");
		in.close();

	}
}
