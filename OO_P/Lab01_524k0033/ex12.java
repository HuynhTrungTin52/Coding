package Lab01_524k0033;

import java.util.Scanner;

public class ex12 {
	
	public static int reverse(int num)
	{
		String str=Integer.toString(num);
		String rts="";
		for(int i=str.length()-1;i>=0;i--)
		{
			rts+=str.charAt(i);
		}
	
		return Integer.parseInt(rts);
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
		System.out.print("Enter a number :");
		int num=in.nextInt();
		int reversedNum=reverse(num);
		System.out.print("The reversed of number above is :"+reversedNum);
	}
	}
}
