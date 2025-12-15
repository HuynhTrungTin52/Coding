package lab08_524k0033;

public class Ex04 {
	public static void main(String[] args) {
		MyPriorityQueue heap = new MyPriorityQueue(6);
		heap.insert(new Prisoners("Alex", 3));
		heap.insert(new Prisoners("Bob", 2));
		heap.insert(new Prisoners("David", 6));
		heap.insert(new Prisoners("Susan", 1));
		System.out.println(heap.extractMax().getName());
		heap.insert(new Prisoners("Mike", 5));
		heap.insert(new Prisoners("Kevin", 4));
		System.out.println(heap.extractMax().getName());
		System.out.println(heap.extractMax().getName());
		heap.insert(new Prisoners("Helen", 0));
		heap.insert(new Prisoners("Paul", 8));
		heap.insert(new Prisoners("Iris", 7));
		System.out.println(heap.extractMax().getName());
	}
}
