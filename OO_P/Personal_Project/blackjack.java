package Personal_Project;

import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class blackjack {



        @SuppressWarnings("ConvertToTryWithResources")
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		char retry='Y';
		int pScore=0,dScore=0;
		while(retry=='Y')
		{
		Bjack player = new Bjack();
		Bjack dealer = new Bjack();
		boolean pBust=false;
		boolean dBust=false;
		dealer.draw();
		System.out.printf("Dealer's(%d pts) hand has : [",dScore);
		dealer.showCards();
		System.out.printf("] (%d + ?)\n",dealer.showVal());
		player.draw(2);
		System.out.printf("Your(%d pts) hand has :[", pScore);
		player.showCards();
		System.out.printf("] (%d)\n",player.showVal());

		if (player.showVal()==21) {
				System.out.print("You won !");
				pScore++;
				System.out.println("Retry ? Y/N");
				retry=in.next().charAt(0);
				if(retry=='N')
				{
					break;
				} else continue;		
		}
		
			
		dealer.draw();
		if (dealer.showVal()==21) {
			
			
				System.out.println("You lost !");
				dScore++;
				System.out.printf("Dealer's hand was :");
				dealer.show();
				System.out.printf("\nRetry ? Y/N");
				retry=in.nextLine().charAt(0);
				if(retry=='Y')
				{
					continue;
				} else break;
			}
		
		char choice;
		System.out.println("Hit or stand ?");
		choice = in.nextLine().charAt(0);
		for (; choice == 'H';) {
			System.out.println("Your turn !");
			player.draw();
			System.out.print("Your hand has :");
			player.show();
			System.out.println("");
			if (player.showVal() > 21) {
				System.out.println("Bust !");
				pBust=true;
				break;
			}
			choice = in.nextLine().charAt(0);

		}
		
		char dChoice=' ';
		System.out.println("Player's turn over !");
		System.out.println("Dealer has :");
		dealer.show();
		System.out.println();
		if(dealer.showVal()<=16 && pBust==false){
		 dChoice = 'H';}
		for (; dChoice == 'H';) {
			System.out.println("Dealer's turn !");
			System.out.printf("Thinking...");
			int j = 0;
			while (j < 3) {
				System.out.printf("\b\b\b");
				System.out.printf(".");
				try {
					TimeUnit.MILLISECONDS.sleep(150);
				} catch (InterruptedException ex) {
				}
				System.out.printf(".");
				try {
					TimeUnit.MILLISECONDS.sleep(150);
				} catch (InterruptedException ex) {
				}
				System.out.printf(".");
				try {
					TimeUnit.MILLISECONDS.sleep(150);
				} catch (InterruptedException ex) {
				}
				j++;
			}
			System.out.printf("\n");
			dealer.draw();
			dealer.show();
			System.out.println("");
			if (dealer.showVal() > 21) {
				System.out.println("Busted !");
				dBust=true;
				break;
			} else 
			if(dealer.showVal()>16 || dealer.showVal()>=player.showVal())
			{
				break;
			}
			
		}
		if ((player.showVal() > dealer.showVal() && player.showVal() <= 21) || dBust==true) {
			
			System.out.println("Player won !");
			pScore++;
		} else if(pBust==true || dealer.showVal()>player.showVal())
		{
			System.out.println("Player lost !");
			dScore++;
		} else if(player.showVal()==dealer.showVal())
		{
			System.out.println("Tied !");
		}
		System.out.println("Retry ? Y/N");
		retry=in.nextLine().charAt(0);
	}
		in.close();
	}
}