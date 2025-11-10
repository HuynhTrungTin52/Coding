package lab08_524k0033;

import java.util.NoSuchElementException;

public class MaxHeap {
	int[] heap;
	int heapSize;
	int maxSize; // maximum size to initialize an heap array

	public MaxHeap(int capacity) {
		heapSize = 0;
		this.maxSize = capacity + 1;
		heap = new int[maxSize];
		heap[0] = -1;
	}

	private int parent(int i) {
		return i / 2;
	}

	private int left(int i) {
		return 2 * i;
	}

	private int right(int i) {
		return 2 * i + 1;
	}

	private void swap(int i, int j) {
		int temp = heap[i];
		heap[i] = heap[j];
		heap[j] = temp;
	}

	public void insert(int key) {
		if (heapSize == maxSize) {
			throw new NoSuchElementException("Overflow Exception"); // Remember to import
																	// java.util.NoSuchElementException;
		}
		heapSize += 1;
		heap[heapSize] = key;

		shiftUp(heapSize);
	}

	private void shiftUp(int i) {
		while (i > 1 && heap[parent(i)] < heap[i]) {
			swap(parent(i), i); // this method you have defined before
			i = parent(i);
		}
	}

	public int extractMax() {
		if (heapSize == 0) {
			throw new NoSuchElementException("Underflow Exception");
		}
		int max = heap[1];
		heap[1] = heap[heapSize];
		heapSize -= 1;
		shiftDown(1);
		return max;
	}

	private void shiftDown(int i) {
		while (i <= heapSize) {
			int max = heap[i];
			int max_id = i;
			if (left(i) <= heapSize && max < heap[left(i)]) {
				max = heap[left(i)];
				max_id = left(i);
			}
			if (right(i) <= heapSize && max < heap[right(i)]) {
				max = heap[right(i)];
				max_id = right(i);
			}
			if (max_id != i) {
				swap(max_id, i);
				i = max_id;
			} else {
				break;
			}
		}
	}
	public static int[] heapSort(int[] arr) {
		MaxHeap heap = new MaxHeap(arr.length);
		int[] res = new int[arr.length];
		for(int value : arr) {
			heap.insert(value);
		}
		
		for(int i=0;i<arr.length;i++) {
			res[i]=heap.extractMax();
		}
		return res;
	}
	public static void main(String[] args) {
		MaxHeap heap = new MaxHeap(10);
		int[] arr= {1,2,3,19,7,26,25,17,29,36};

		for(int value :arr) {
			heap.insert(value);
		}
		for (int value : heap.heap) {
			System.out.print(value + " ");
		}
		System.out.println();
		heap.extractMax();
		for(int value : heap.heap) {
			System.out.print(value+" ");
		}
	}
}
