
import java.util.Scanner;

public class Ex05 {
	public static int decimalToBinary(int n) {
		if (n == 0) {
			return 0;
		}
		return decimalToBinary(n / 2) * 10 + (n % 2);
	}

	public static void main(String[] args) {
		Scanner in = new java.util.Scanner(System.in);
		System.out.print("Enter a decimal number: ");
		int n = in.nextInt();
		System.out.println("Binary representation: " + decimalToBinary(n));
		in.close();
	}
}
