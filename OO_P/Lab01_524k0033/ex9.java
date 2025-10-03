package Lab01_524k0033;

import java.util.Scanner;

public class ex9 {
	public static int hailStone(int n)
	{
		if(n==1)
		{
			System.out.print("n=1, terminating program");
			return 1;
		}
		if(n%2==0)
		{
			System.out.printf("%d is even, divided by 2 is :%d\n",n,n/2);
			return hailStone(n/2);
			
		}else {
			System.out.printf("%d is odd, multiplying by 3 and adding 1 :%d\n",n,n*3+1);
			return hailStone(n*3+1);
		}
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter n :");
			int n=in.nextInt();
			hailStone(n);
		}
	}
}
