package lab03_524k0033;


import java.util.Scanner;

public class Ex04 {

	public static int sum2iPlus1(int n) {
		if (n == 1)
			return 3;
		return (2 * n + 1) + sum2iPlus1(n - 1);
	}

	public static int sumFactorials(int n) {
		if (n == 1)
			return 1;
		return factorial(n) + sumFactorials(n - 1);
	}

	public static int prodFactorials(int n) {
		if (n == 1)
			return 1;
		return factorial(n) * prodFactorials(n - 1);
	}

	public static int factorial(int n) {
		if (n == 1)
			return 1;
		return n * factorial(n - 1);
	}

	public static int P(int n, int r) {
		if (n >= r && r > 0)
			return n * P(n - 1, r - 1);
		else
			return 1;
	}

	public static int P(int n) {
		if (n == 1)
			return 3;
		return (int) Math.pow(2, n) + n * n + P(n - 1);
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);

		System.out.print("Enter an integer n: ");
		int n = in.nextInt();

		System.out.print("Enter another integer r for P(n, r): ");
		int r = in.nextInt();

		System.out.println("sum2iPlus1(" + n + ") = " + sum2iPlus1(n));
		System.out.println("sumFactorials(" + n + ") = " + sumFactorials(n));
		System.out.println("prodFactorials(" + n + ") = " + prodFactorials(n));
		System.out.println("factorial(" + n + ") = " + factorial(n));
		System.out.println("P(" + n + ", " + r + ") = " + P(n, r));
		System.out.println("P(" + n + ") = " + P(n));

		in.close();
	}
}
