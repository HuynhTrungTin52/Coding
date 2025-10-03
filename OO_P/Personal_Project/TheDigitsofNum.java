package Personal_Project;
import java.util.*;

public class TheDigitsofNum {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a number to get the sum and product of digits :");
		int num=in.nextInt();
		int sum=0,prod=1;
		while(num!=0)
		{
			int dig=num%10;
			sum+=dig;
			prod*=dig;
			num/=10;
		}
		System.out.printf("Sum : %d\nProduct : %d",sum,prod);
		in.close();
	}
}
