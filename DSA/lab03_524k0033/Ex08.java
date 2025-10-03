public class Ex08 {
	public static void main(String[] args) {
		MyLinkedList<Integer> list = new MyLinkedList<>();
		for (int i = 0; i <= 10; i += 2) {
			list.addLast(i);
		}
		list.addSortedList(5);
		list.print();
	}
}
