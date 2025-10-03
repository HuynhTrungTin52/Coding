package Personal_Project;

import java.util.Scanner;

public class debate {
	
	public static boolean isFakePrime(int n)
	{
		return !(n%2==0 || n%3 ==0 || n%5==0 || n%11==0 || Math.sqrt(n) % 1==0);
	}
	public static boolean isPrime(int n)
	{
		for(int i=2;i<n/2;i++)
		{
			if(n%i==0) return false;
		}
		return true;
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
		System.out.print("Enter n :");
		int n=in.nextInt();
		for(int i=2;i<=n;i++)
		{
		if(isFakePrime(i))
		{
			if(!isPrime(i)) System.out.printf("%d ",i);
		}
			

		}
	}
	}
}
