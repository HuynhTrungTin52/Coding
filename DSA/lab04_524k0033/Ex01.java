import java.util.Arrays;

public class Ex01 {
	public static int[] SelectionSort(int[] arrayInt) {
		// 1. Find the index of the smallest unsorted item.
		// 2. Swap the current item with the smallest unsorted one.
		// 3. Exclude the smallest item which we found in step 2 and go to step 1.

		for (int i = 0; i < arrayInt.length - 1; i++) {
			int min_ind = i;
			for (int j = i + 1; j < arrayInt.length; j++) {
				if (arrayInt[j] < arrayInt[min_ind]) {
					min_ind = j;
				}
			}
			int temp = arrayInt[min_ind];
			arrayInt[min_ind] = arrayInt[i];
			arrayInt[i] = temp;
		}
		return arrayInt;
	}

	public static int[] BubbleSort(int[] arrayInt) {
		for (int i = 0; i < arrayInt.length - 1; i++) {
			for (int j = 0; j < arrayInt.length - i - 1; j++) {
				if (arrayInt[j] > arrayInt[j + 1]) {
					int temp = arrayInt[j];
					arrayInt[j] = arrayInt[j + 1];
					arrayInt[j + 1] = temp;
				}
			}
		}
		return arrayInt;
	}

	public static int[] InsertionSort(int[] arrayInt) {
		for (int i = 1; i < arrayInt.length; i++) {
			int key = arrayInt[i];
			int j = i - 1;
			while (j >= 0 && arrayInt[j] > key) {
				arrayInt[j + 1] = arrayInt[j];
				j--;
			}
			arrayInt[j + 1] = key;
		}
		return arrayInt;
	}

	private static void merge(int arr[], int l, int m, int r) {
		{
			// Find sizes of two sub-arrays to be merged
			int n1 = m - l + 1;
			int n2 = r - m;
			// Create temp arrays
			int L[] = new int[n1];
			int R[] = new int[n2];
			// Copy data to temp arrays
			for (int i = 0; i < n1; i++)
				L[i] = arr[l + i];
			for (int j = 0; j < n2; j++)
				R[j] = arr[m + 1 + j];
			/* Merge the temp arrays */
			// Initial indexes of first and second sub-arrays
			int i = 0, j = 0;
			// Initial index of merged sub-array
			int k = l;
			while (i < n1 && j < n2) {
				if (L[i] <= R[j]) {
					arr[k] = L[i];
					i++;
				} else {
					arr[k] = R[j];

					j++;
				}
				k++;
			}
			// Copy remaining elements of L[] if any
			while (i < n1) {
				arr[k] = L[i];
				i++;
				k++;
			}
			// Copy remaining elements of R[] if any
			while (j < n2) {
				arr[k] = R[j];
				j++;
				k++;
			}
		}
	}

	// Main function of merge sort that sorts arr[first..last] using merge() method
	public static void MergeSort(int[] arr, int first, int last) {
		if (first < last) {
			// Find the middle point
			int middle = (first + last) / 2;
			// Sort first and second halves
			MergeSort(arr, first, middle);
			MergeSort(arr, middle + 1, last);
			// Merge the sorted halves
			merge(arr, first, middle, last);
		}
	}

	/*
	 * This function takes last element as pivot , places the pivot
	 * element at its correct position in sorted array , and places all
	 * smaller (smaller than pivot) to left of pivot and all greater
	 * elements to right of pivot
	 */
	private static int partition(int[] arr, int low, int high) {
		int pivot = arr[high];
		// index of smaller element
		int i = (low - 1);
		for (int j = low; j < high; j++) {
			// If current element is smaller than or equal to pivot
			if (arr[j] <= pivot) {

				i++;
				// swap arr[i] and arr[j]
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
		// swap arr[i+1] and arr[high] (or pivot)
		int temp = arr[i + 1];
		arr[i + 1] = arr[high];
		arr[high] = temp;
		return i + 1;
	}

	// The main function that implements QuickSort algorithm
	// arr[] --> Array to be sorted ,
	// low --> Starting index ,
	// high --> Ending index
	public static void QuickSort(int[] arr, int low, int high) {
		if (low < high) {
			// pi is partitioning index , arr[pi] is now at right place
			int pi = partition(arr, low, high);
			// Recursively sort elements before partition and after partition
			QuickSort(arr, low, pi - 1);
			QuickSort(arr, pi + 1, high);
		}
	}

	public static void main(String[] args) {
		int[] arrayInt = new int[10];
		for (int i = 0; i < arrayInt.length; i++) {
			arrayInt[i] = (int) (Math.random() * 11);
		}
		System.out.println(Arrays.toString(arrayInt));
		QuickSort(arrayInt, 0, 9);
		System.out.print(Arrays.toString(arrayInt));
	}
}