package Lab01_524k0033;

import java.util.Scanner;

public class ex6 {
	public static int findMin(int num1,int num2,int num3)
	{
		if(num1<num2 && num1 <num3) return num1;
		if(num2<num1 && num2<num3) return num2;
		if(num3<num1 && num3<num2) return num3;
		return num1;
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter three numbers :");
			int num1=in.nextInt(),num2=in.nextInt(),num3=in.nextInt();
			int min=findMin(num1,num2,num3);
			int temp=Math.min(num1,num2);
			int min2=Math.min(temp,num3);
			System.out.println("The smallest number is :"+min);
			System.out.print("The smallest number is :"+min2);
		}
	}
}
