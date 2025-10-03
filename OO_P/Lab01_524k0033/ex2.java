package Lab01_524k0033;

import java.util.Scanner;

public class ex2 {
	public static void main(String[] args) {
		//area =1/2 * base * height
		try(Scanner in = new Scanner(System.in)){
		System.out.print("Enter the base of the triangle :");
		float base = in.nextFloat();
		System.out.print("Enter the height of the triangle :");
		float height = in.nextFloat();
		float area = (float)1/2*base*height;
		System.out.print("The area of the triangle is :"+area);			
	}
	}
}
