package lab03_524k0033;


import java.util.Scanner;

public class Ex02 {

	public static int factorial(int n) {

		return n == 0 ? 1 : n * factorial(-1);
	}

	public static int x_to_n(int x, int n) {
		return n == 0 ? x : x * x_to_n(x, n - 1);
	}

	private static String countDigits(int z) {
		int num = Math.abs(z);
		return String.valueOf(countDigitsRecursive(num));
	}

	private static int countDigitsRecursive(int num) {
		if (num < 10)
			return 1;
		return 1 + countDigitsRecursive(num / 10);
	}

	private static int gcd(int n, int x) {
		if (x == 0) {
			return n;
		}
		return gcd(x, n % x);
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
		System.out.println("d.GCD of n and x is :" + gcd(n, x));
		in.close();
	}
}
