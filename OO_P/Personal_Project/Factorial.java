package Personal_Project;
import java.util.*;

public class Factorial {
	public static int facto(int num)
	{
		if( num==1) return 1;

		return num*facto(num-1);
	}
	public static void main(String[] args) {
            try (Scanner in = new Scanner(System.in)) {
                System.out.print("Enter a number :");
                int num=in.nextInt();
                int res=facto(num);
                System.out.print("The factorial number is :" + res);
            }
	}
}
