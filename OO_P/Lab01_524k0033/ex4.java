package Lab01_524k0033;

import java.util.Scanner;


public class ex4 {
	public static float CeltoFar(float temp)
{
	float res=(temp*(float)9/5)+32;
	return res;
}
public static float FartoCel(float temp)
{
	float res=(temp-32)*(float)5*9;
	return res;
}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.println("Would you like to :");
			System.out.println("1.Celcius to Farenheit.");
			System.out.println("2.Farenheit to Celcius.");
			int choice=in.nextInt();
			System.out.print("Enter the temperature to convert :");
			float temp=in.nextFloat();
			if(choice==1)
			{
				System.out.printf("%.2fC -> %.2fF",temp,CeltoFar(temp));
			} else if(choice==2)
			{
				System.out.printf("%.2fF -> %.2fC",temp,FartoCel(temp));
			}
		}
	}
}
