public class Sorting {
	public static void main(String[] args) {
		int[] arr = {5, 2, 9, 1, 5, 6,7,4,1,0,19,29,12};

		System.out.println("Original array:");
		printArray(arr);

		int[] selectionSorted = arr.clone();
		selectionSort(selectionSorted);
		System.out.println("Selection Sort:");
		printArray(selectionSorted);

		int[] bubbleSorted = arr.clone();
		bubbleSort(bubbleSorted);
		System.out.println("Bubble Sort:");
		printArray(bubbleSorted);

		int[] insertionSorted = arr.clone();
		insertionSort(insertionSorted);
		System.out.println("Insertion Sort:");
		printArray(insertionSorted);
		}

		public static void selectionSort(int[] arr) {
			int n = arr.length;
			for (int i = 0; i < n - 1; i++) {
				int minIdx = i;
				for (int j = i + 1; j < n; j++) {
					if (arr[j] < arr[minIdx]) {
						minIdx = j;
					}
				}
				int temp = arr[minIdx];
				arr[minIdx] = arr[i];
				arr[i] = temp;
			}
		}

		public static void bubbleSort(int[] arr) {
			int n = arr.length;
			for (int i = 0; i < n - 1; i++) {
				for (int j = 0; j < n - i - 1; j++) {
					if (arr[j] > arr[j + 1]) {
						int temp = arr[j];
						arr[j] = arr[j + 1];
						arr[j + 1] = temp;
					}
				}
			}
		}

		public static void insertionSort(int[] arr) {
			int n = arr.length;
			for (int i = 1; i < n; i++) {
				int key = arr[i];
				int j = i - 1;
				while (j >= 0 && arr[j] > key) {
					arr[j + 1] = arr[j];
					j--;
				}
				arr[j + 1] = key;
			}
		}

		public static void printArray(int[] arr) {
			for (int num : arr) {
				System.out.print(num + " ");
			}
			System.out.println();
		}
	}
