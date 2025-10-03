package Lab01_524k0033;

import java.util.Scanner;


public class ex3 {

	public static float remainder(float a, float b)
	{
		return a %b;
	}

	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter a and b to see the remainder of a/b :");
			float a=in.nextFloat();
			float b=in.nextFloat();
			float answer=remainder(a,b);
			
			System.out.print("Remainder of a/b is :"+answer);
		}
	}
}
