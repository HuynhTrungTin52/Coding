public class Recursion3 {
	public static void main(String[] args) {
		System.out.println("A(a) Recursive: " + aRecursive(3));
		System.out.println("A(a) Iterative: " + aIterative(3));

		System.out.println("A(b) Recursive: " + bRecursive(100));
		System.out.println("A(b) Iterative: " + bIterative(100));

		System.out.println("A(c) Recursive: " + cRecursive(5, 3));
		System.out.println("A(c) Iterative: " + cIterative(5, 3));

		System.out.println("F(d) Recursive: " + dRecursive(7));
		System.out.println("F(d) Iterative: " + dIterative(7));
	}

	public static double aRecursive(int n) {
		if (n <= 1) return 1;
		return 2 -  (1.0/2 * aRecursive(n - 1));
	}

	public static double aIterative(int n) {
		double result = 1;
		for (int i = 2; i <= n; i++) {
			result = 2 - 0.5 * result;
		}
		return result;
	}

	public static double bRecursive(int n) {
		if (n <= 1) return n;
		return n + bRecursive(n/10);
	}

	public static int bIterative(int n) {
		int sum = 0;
		while (n > 1) {
			sum += n;
			n /= 10;
		}
		sum += n; 
		return sum;
	}

	public static int cRecursive(int n, int k) {
		if (k == 0) return 1;
		return n * cRecursive(n, k - 1);
	}

	public static int cIterative(int n, int k) {
		int result = 1;
		for (int i = 0; i < k; i++) {
			result *= n;
		}
		return result;
	}

	public static int dRecursive(int n) {
		if (n <= 1) return n;
		return dRecursive(n - 1) + dRecursive(n - 2);
	}

	public static int dIterative(int n) {
		if (n <= 1) return n;
		int a = 0, b = 1;
		for (int i = 2; i <= n; i++) {
			int temp = a + b;
			a = b;
			b = temp;
		}
		return b;
	}
	}	
