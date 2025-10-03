package Personal_Project;
import java.util.Scanner;

public class Classfirst{

	public static void main(String[] args)
	{
            try ( //cel=5/9*(faren-32)
                    Scanner scVar = new Scanner(System.in)) {
                double faren,cel;
                System.out.print("Please enter your farenheit degree :");
                faren=scVar.nextDouble();
                cel=5.0/9*(faren-32);
                System.out.printf("Celcius :%.3f",cel);
            }
	}
}