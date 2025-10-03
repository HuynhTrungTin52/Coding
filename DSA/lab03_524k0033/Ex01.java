
import java.util.Scanner;

public class Ex01 {

	public static int factorial(int n) {
		int fac = 1;
		for (int i = 0; i < n; n--) {
			fac *= n;
		}
		return fac;
	}

	public static int x_to_n(int x, int n) {
		if (n == 0) {
			return 1;
		}
		int res = x;
		for (int i = 1; i < n; i++) {
			res *= x;
		}
		return res;
	}

	public static boolean isPrime(int z) {
		for (int i = 2; i <= Math.sqrt(z); i++) {
			if (z % i == 0) {
				return false;
			}
		}
		return true;
	}

	private static String countDigits(int z) {
		int count = 0;
		int num = Math.abs(z);
		if (num == 0) {
			count = 1;
		} else {
			while (num > 0) {
				num /= 10;
				count++;
			}
		}
		return String.valueOf(count);
	}

	private static int gcd(int n, int x) {
		while (x != 0) {
			int temp = x;
			x = n % x;
			n = temp;
		}
		return n;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		System.out.print("Enter n: ");
		int n = in.nextInt();
		System.out.print("Enter x: ");
		int x = in.nextInt();
		System.out.print("Enter a positive integer z: ");
		int z = in.nextInt();
		System.out.println("a.Factorial of n: " + factorial(n));
		System.out.println("b.x to the power of n: " + x_to_n(x, n));
		System.out.println("c.Counting the digits inside the number: " + countDigits(z));
		System.out.println("d.Check if n(must be positive) is a prime or not :" + isPrime(z));
		System.out.println("e.GCD of n and x is :" + gcd(n, x));
		in.close();
	}
}
