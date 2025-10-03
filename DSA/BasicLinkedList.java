import java.util.*;
class BasicLinkedList <E> implements ListInterfaces <E> {
	private ListNode <E> head = null;
	private int num_nodes = 0;

        @Override
	public boolean isEmpty() { return (num_nodes == 0); }

        @Override
	public int size() { return num_nodes; }

        @Override
	public E getFirst() throws NoSuchElementException {
		if (head == null) 
			throw new NoSuchElementException("can't get from an empty list");
		else return head.getElement();
	}

        @Override
	public boolean contains(E item) {
		for (ListNode <E> n = head; n != null; n = n.getNext())
			if (n.getElement().equals(item)) return true;
		return false;
	}
	//One of the most popular way to traverse through a Linked List(Loop with 1 variable)
	//TODO : Write this back into NB and review
        @Override
	public void addFirst(E item) {
		head = new ListNode <> (item, head);
 		//ListNode p = new ListNode (item);
		//p.setNext(head);//p.next = head
		//head = p;

		num_nodes++;
	}

        @Override
	public E removeFirst() throws NoSuchElementException {
		ListNode <E> ln;
		if (head == null) 
			throw new NoSuchElementException("can't remove from empty list");
		else { 
			ln = head;
			head = head.getNext();
			num_nodes--;
			return ln.getElement();
		}
	}

	@Override
	public void print() throws NoSuchElementException {
		if (head == null)
			throw new NoSuchElementException("Nothing to print...");

		ListNode <E> ln = head;
		System.out.print("List is: " + ln.getElement());
		for (int i=1; i < num_nodes; i++) {
			ln = ln.getNext();
			System.out.print(", " + ln.getElement());
		}
		System.out.println(".");
	}

    @Override
    public E removeLast() throws NoSuchElementException {
        if (head == null) 
			throw new NoSuchElementException("can't remove from empty list");
		else if(num_nodes==1) {
			return removeFirst();
		} else { 
			ListNode <E> prev=null;
			ListNode <E> curr = head;
			for(; curr!=null;curr=curr.getNext()) {
				prev=prev.getNext();
				curr=curr.getNext();
			}
			
			prev.setNext(null);
			return curr.getElement();
		}
    }
}