package Personal_Project;
import java.util.Scanner;
//Tin lam
public class AproxPi {
	public static void main(String[] args) {
		Scanner in= new Scanner(System.in);
		System.out.print("Enter the term to approximate Pi :");
		int term=in.nextInt();
		double res=0;
		for(int i=1,j=1;i<=term;i++,j+=2)
		{
			if(i%2!=0)
			{
				res+=4.0/j;
			}else res-=4.0/j;
		}
		System.out.printf("The Pi approximated to :%.6f",res);
		in.close();
	}
}
