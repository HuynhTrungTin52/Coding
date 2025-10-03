package Personal_Project;
import java.util.*;

public class PrimeChecker {
	public static boolean pChecker(int num)
	{
		for(int i=2;i<num;i++)
		{
			if(num%i==0) return false;
		}
	return true;
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a number to see if it's a prime :");
		int num=in.nextInt();
		boolean isPrime=pChecker(num);
		if(isPrime==true) System.out.printf("%d is a prime number",num); else System.out.printf("%d is NOT a prime number",num);


		in.close();
	}
}
