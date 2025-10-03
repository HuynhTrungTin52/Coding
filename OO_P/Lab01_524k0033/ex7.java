package Lab01_524k0033;

import java.util.Scanner;

public class ex7 {

	public static boolean isAlphanum(String str)
	{
		boolean letter=false,number=false;
		for(int i=0;i<str.length();i++)
		{
			if((str.charAt(i)>='a' && str.charAt(i)<='z') || (str.charAt(i)>='A' && str.charAt(i)<='Z')) letter =true;
			if(str.charAt(i)>='0' && str.charAt(i)<='9') number=true;
		}
	return letter && number;
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter a string :");
			String str=in.nextLine();
			boolean isAlpha = isAlphanum(str);
			if(isAlpha) System.out.print("The string above is Alphanumeric"); else System.out.print("The string above is NOT Alphanumeric");
		}
	}
}
