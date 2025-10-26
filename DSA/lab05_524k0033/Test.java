package lab05_524k0033;

public class Test {
	public static void main(String[] args) {
		Integer[] arr={20,19,18,17,16,5,1,-200};
		IntLinkedList list = new IntLinkedList();
		for (Integer value : arr) {
			list.addFirst(value);
		}
		list.print();
		// list.removeAt(3);
		// list.print();

		// System.out.print(list.countOdd());
		System.out.print(list.checkSorted());
		
	}
}
