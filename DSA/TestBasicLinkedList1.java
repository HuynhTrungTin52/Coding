import java.util.*;

public class TestBasicLinkedList1 {
	public static void main(String [] args) 
		                   throws NoSuchElementException {
		BasicLinkedList <String> list1 = new BasicLinkedList <String>();
		list1.addFirst("aaa");
		list1.addFirst("bbb");
		list1.addFirst("ccc");
		list1.print();

		System.out.println("Testing removal");
		list1.removeFirst();
		list1.print();

		if (list1.contains("aaa")) 
			list1.addFirst("xxxx");
		list1.print();

		BasicLinkedList <Integer> list2 = new BasicLinkedList <Integer>();

		list2.addFirst(34);
		list2.addFirst(12);
		list2.addFirst(9);
		list2.print();

		System.out.println("Testing removal");
		list2.removeFirst();
		list2.print();
		list2.removeLast();
		list2.print();
	}
	

}
