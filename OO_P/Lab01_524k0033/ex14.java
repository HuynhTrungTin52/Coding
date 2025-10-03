package Lab01_524k0033;

import java.util.Scanner;

public class ex14{

	public static void main(String[] args) {
		//Coca, Pepsi, Spirte, Snack
		//2		2	   2	   1.5
		try(Scanner in = new Scanner(System.in)){
		char choice=' ';
		float money;
		while (choice!='5') { 
			System.out.println("----Menu----");
			System.out.println("1.Coca");
			System.out.println("2.Pepsi");
			System.out.println("3.Sprite");
			System.out.println("4.Snack");
			System.out.println("5.Shut down");
			System.out.print("Please enter a number :");
			choice=in.next().charAt(0);

			switch(choice)
			{
				case '1' -> {
					System.out.print("The price of Coca is 2$, please enter the amount of money :");
					money=in.nextFloat();
					if(money>=2)
					{
						System.out.printf("Your change is %.2f\n",money-2);
					} else {
						System.out.println("Not enough money, please select again");
					}
				}
				case '2' -> {
					System.out.print("The price of Pepsi is 2$, please enter the amount of money :");
					money=in.nextFloat();
					if(money>=2)
					{
						System.out.printf("Your change is %.2f\n",money-2);
					}else {
						System.out.println("Not enough money, please select again");
					}
				}
				case '3' -> {
					System.out.print("The price of Sprite is 2$, please enter the amount of money :");
					money=in.nextFloat();
					if(money>=2)
					{
						System.out.printf("Your change is %.2f\n",money-2);
					}else {
						System.out.println("Not enough money, please select again");
					}
				}
				case '4' -> {
					System.out.print("The price of Snack is 2$, please enter the amount of money :");
					money=in.nextFloat();
					if(money>=1.5)
					{
						System.out.printf("Your change is %.2f\n",money-1.5);
					}else {
						System.out.println("Not enough money, please select again");
					}
				}
				default -> {
					System.out.print("Please enter a valid number");
					
				}
				
			}
		}
	System.out.print("Shutting down machine");
	}
	}
}