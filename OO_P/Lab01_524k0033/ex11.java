package Lab01_524k0033;

import java.util.Scanner;

public class ex11 {
	public static int getLength(int num)
	{
		String str=Integer.toString(num);
		return str.length();
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter a number :");
			int num=in.nextInt();
			int length=getLength(num);
			System.out.print("The length of the number above is:"+length);
		}
	}
}
