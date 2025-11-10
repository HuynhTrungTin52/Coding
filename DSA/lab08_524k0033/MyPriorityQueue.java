package lab08_524k0033;

import java.util.NoSuchElementException;

public class MyPriorityQueue {
	Prisoners[] heap;
	int heapSize;
	int maxSize; // maximum size to initialize an heap array

	public MyPriorityQueue(int capacity) {
		heapSize = 0;
		this.maxSize = capacity + 1;
		heap = (Prisoners[]) new Object[maxSize];
		heap[0] = null;
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
		Prisoners temp = heap[i];
		heap[i] = heap[j];
		heap[j] = temp;
	}

	public void insert(Prisoners key) {
		if (heapSize == maxSize - 1) {
			throw new NoSuchElementException("Overflow Exception");
		}
		heapSize += 1;
		heap[heapSize] = key;

		shiftUp(heapSize);
	}

	private void shiftUp(int i) {
		while (i > 1 && heap[parent(i)].compareTo(heap[i]) < 0) {
			swap(parent(i), i);
			i = parent(i);
		}
	}

	public Prisoners extractMax() {
		if (heapSize == 0) {
			throw new NoSuchElementException("Underflow Exception");
		}
		Prisoners max = heap[1];
		heap[1] = heap[heapSize];
		heap[heapSize] = null;
		heapSize -= 1;
		shiftDown(1);
		return max;
	}

	private void shiftDown(int i) {
		while (i <= heapSize) {
			Prisoners max = heap[i];
			int max_id = i;
			if (left(i) <= heapSize && max.compareTo(heap[left(i)]) < 0) {
				max = heap[left(i)];
				max_id = left(i);
			}
			if (right(i) <= heapSize && max.compareTo(heap[right(i)]) < 0) {
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
	public static  Prisoners[] heapSort(Prisoners[] arr) {
		MyPriorityQueue heap = new MyPriorityQueue(arr.length);
		Prisoners[] res = (Prisoners[]) new Object[arr.length];
		for (Prisoners value : arr) {
			heap.insert(value);
		}
		
		for (int i = 0; i < arr.length; i++) {
			res[i] = heap.extractMax();
		}
		return res;
	}
}
