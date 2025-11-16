public class Ex03 {
	public static void arrPrint(int[] arr) {
		for(int value : arr) {
			System.out.print(value+" ");
		}
	}
	public static void main(String[] args) {
		int[] arr ={15, 23, 18, 63, 21, 35, 36, 21, 66, 12, 42, 35, 75, 23, 64, 78, 39};
		System.out.print("Given an array :");
		arrPrint(arr);
		System.out.println();
		System.out.print("Using heapsort to sort descendingly:");
		arrPrint(MaxHeap.heapSort(arr));
		System.out.println();
		System.out.print("Using heapsort to sort ascendingly:");
		arrPrint(MinHeap.heapSort(arr));

		System.out.println();
		System.out.print("Using heapsort to sort descendingly FAST:");
		MaxHeap.heapSortFast(arr);
		arrPrint(arr);

		System.out.println();
		System.out.print("Using heapsort to sort ascendingly FAST:");
		MinHeap.heapSortFast(arr);
		arrPrint(arr);

		
	}
}
