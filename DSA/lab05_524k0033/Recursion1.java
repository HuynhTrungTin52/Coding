package lab05_524k0033;

public class Recursion1 {
	public static void main(String[] args) {
		System.out.println("prod_recur: " + prod_recur(5, 3));
		System.out.println("bin2dec: " + bin2dec(1000, 0));
		System.out.println("maxDigit: " + maxDigit(1231415));
		int[] arr = {2, 7, 3, 9, 5};
		int size=arr.length;
		System.out.println("maxElement: " + maxElement(arr, size));
		System.out.println("search: " + search(arr, size, 9));
		}

		// (a)
		public static double prod_recur(int a, int b) {
			if (b == 0) return 0;
			if (b > 0) return a + prod_recur(a, b - 1);
			return -prod_recur(a, -b);
		}

		// (b)
		public static int bin2dec(int n, int exp) {
			if (n == 0) return 0;
			return (n % 10) * (int)Math.pow(2, exp) + bin2dec(n / 10, exp + 1);
		}

		// (c)
		public static int maxDigit(int n) {
			if (n < 10) return n;
			int last = n % 10;
			int rest = maxDigit(n / 10);
			return Math.max(last, rest);
		}

		// (d)
		public static int maxElement(int a[], int n) {
			if (n == 1) return a[0];
			return Math.max(a[n - 1], maxElement(a, n - 1));
		}

		// (e)
		public static int search(int a[], int n, int key) {
			if (n == 0) return -1;
			if (a[n - 1] == key) return n - 1;
			return search(a, n - 1, key);
		}
	}

