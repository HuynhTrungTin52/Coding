import java.util.Random;

public class Ex06 {
	public static int findMin(int[] arr, int size) {
		if (size == 0)
			throw new IllegalArgumentException("Array is empty");
		int min = arr[0];
		for (int i = 1; i < size; i++) {
			if (arr[i] < min) {
				min = arr[i];
			}
		}
		return min;
	}

	public static int sumArray(int[] arr, int size) {
		int sum = 0;
		for (int i = 0; i < size; i++) {
			sum += arr[i];
		}
		return sum;
	}

	public static int countEven(int[] arr, int size) {
		int count = 0;
		for (int i = 0; i < size; i++) {
			if (arr[i] % 2 == 0) {
				count++;
			}
		}
		return count;
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
