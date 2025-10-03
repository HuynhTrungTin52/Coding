
import java.util.Scanner;

class Ex03 {
	public static boolean checkPrime(int n, int d) {
		if (n < 2)
			return false;
		if (d * d > n)
			return true;
		if (n % d == 0)
			return false;
		return checkPrime(n, d + 1);
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		System.out.print("Enter n: ");
		int n = in.nextInt();
		System.out.print("Checking if n is a prime:" + checkPrime(n, 2));

		in.close();
	}
}