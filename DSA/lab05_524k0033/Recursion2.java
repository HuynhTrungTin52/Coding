package lab05_524k0033;

public class Recursion2 {
public static void main(String[] args) {
	int n = 5;

	// (a) Sum of 2^i from i=1 to n
	System.out.println("a) Iterative: " + sumPowerOfTwoIter(n));
	System.out.println("a) Recursive: " + sumPowerOfTwoRec(n));

	// (b) Sum of (x+1)/2 from x=0 to n
	System.out.println("b) Iterative: " + sumXPlusOneOverTwoIter(n));
	System.out.println("b) Recursive: " + sumXPlusOneOverTwoRec(n));

	// (c) Sum of i!/(i-1)! from i=1 to n
	System.out.println("c) Iterative: " + sumFactorialDivIter(n));
	System.out.println("c) Recursive: " + sumFactorialDivRec(n));

	// (d) Sum of x*(x-1) from x=1 to n
	System.out.println("d) Iterative: " + sumXTimesXMinusOneIter(n));
	System.out.println("d) Recursive: " + sumXTimesXMinusOneRec(n));

	// (e) Product of x from x=1 to n (factorial)
	System.out.println("e) Iterative: " + productIter(n));
	System.out.println("e) Recursive: " + productRec(n));
	}

	// (a)
	static int sumPowerOfTwoIter(int n) {
		int sum = 0;
		for (int i = 1; i <= n; i++) sum += Math.pow(2, i);
		return sum;
	}
	static int sumPowerOfTwoRec(int n) {
		if (n == 0) return 0;
		return (int)Math.pow(2, n) + sumPowerOfTwoRec(n - 1);
	}

	// (b)
	static double sumXPlusOneOverTwoIter(int n) {
		double sum = 0;
		for (int x = 0; x <= n; x++) sum += (x + 1) / 2.0;
		return sum;
	}
	static double sumXPlusOneOverTwoRec(int n) {
		if (n < 0) return 0;
		return (n + 1) / 2.0 + sumXPlusOneOverTwoRec(n - 1);
	}

	// (c)
	static int sumFactorialDivIter(int n) {
		int sum = 0;
		for (int i = 1; i <= n; i++) sum += i;
		return sum;
	}
	static int sumFactorialDivRec(int n) {
		if (n == 0) return 0;
		return n + sumFactorialDivRec(n - 1);
	}

	// (d)
	static int sumXTimesXMinusOneIter(int n) {
		int sum = 0;
		for (int x = 1; x <= n; x++) sum += x * (x - 1);
		return sum;
	}
	static int sumXTimesXMinusOneRec(int n) {
		if (n == 0) return 0;
		return n * (n - 1) + sumXTimesXMinusOneRec(n - 1);
	}

	// (e)
	static int productIter(int n) {
		int prod = 1;
		for (int x = 1; x <= n; x++) prod *= x;
		return prod;
	}
	static int productRec(int n) {
		if (n <= 1) return 1;
		return n * productRec(n - 1);
	}
}

