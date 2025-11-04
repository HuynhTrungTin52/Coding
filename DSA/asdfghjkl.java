import java.util.PriorityQueue;

public class asdfghjkl {
	public static void main(String[] args) {
		PriorityQueue<Integer> heap = new PriorityQueue<>();
		int[] a={33, 96, 14, 29, 78, 94, 34, 42, 93, 99};
		for(int value :a) {
			heap.offer(value);
		}

		while(!heap.isEmpty()) {
			System.out.println(heap.poll());
		}
	}
}