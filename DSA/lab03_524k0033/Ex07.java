package lab03_524k0033;

import java.util.Random;

public class Ex07 {
	public static int findMin(int[] arr, int size) {
		if (size == 0) {
			throw new IllegalArgumentException("Array is empty");
		}
		return findMinHelper(arr, size, 1, arr[0]);
	}

	private static int findMinHelper(int[] arr, int size, int index, int currentMin) {
		if (index >= size) {
			return currentMin;
		}

		if (arr[index] < currentMin) {
			currentMin = arr[index];
		}

		return findMinHelper(arr, size, index + 1, currentMin);
	}

	public static int sumArray(int[] arr, int size) {

		return sumArrayHelper(arr, size, 0);
	}

	private static int sumArrayHelper(int[] arr, int size, int index) {

		if (index >= size) {
			return 0;
		}

		return arr[index] + sumArrayHelper(arr, size, index + 1);
	}

	public static int countEven(int[] arr, int size) {

		return countEvenHelper(arr, size, 0);
	}

	private static int countEvenHelper(int[] arr, int size, int index) {

		if (index >= size) {
			return 0;
		}

		int currentCount = 0;
		if (arr[index] % 2 == 0) {
			currentCount = 1;
		}
		return currentCount + countEvenHelper(arr, size, index + 1);
	}

	public static void main(String[] args) {
		int size = 10;
		int[] arr = new int[size];
		Random rand = new Random();
		for (int i = 0; i < size; i++) {
			arr[i] = rand.nextInt(100);
		}
		System.out.print("Array: ");
		for (int num : arr) {
			System.out.print(num + " ");
		}
		System.out.println();
		System.out.println("Minimum: " + findMin(arr, size));
		System.out.println("Sum: " + sumArray(arr, size));
		System.out.println("Count of even numbers: " + countEven(arr, size));
	}
}
