package Lab01_524k0033;

import java.util.Scanner;

public class ex13 {

	public static boolean isPalin(int num)
	{
		String str=Integer.toString(num);
		
		for(int i=0,j=str.length()-1;i<=str.length()/2;i++,j--)
		{
			if(str.charAt(i)!=str.charAt(j)) return false;
		}
	
		return true;
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
		System.out.print("Enter a number :");
		int num=in.nextInt();
		if(isPalin(num)) System.out.printf("%d is a palindrome",num); else System.out.printf("%d is NOT a palindrome",num);
	}
	}
}
