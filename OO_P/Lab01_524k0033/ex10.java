package Lab01_524k0033;

import java.util.Scanner;

public class ex10 {
	public static int firstAndLast(int num)
	{
		String str=Integer.toString(num);
		int first=Character.getNumericValue(str.charAt(0));
		int last=Character.getNumericValue(str.charAt(str.length()-1));
		return first+last;
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter a number :");
			int num=in.nextInt();
			int res=firstAndLast(num);
			System.out.print("The first and last number combined is :"+res);
		}
	}
}
