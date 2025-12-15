import java.util.*;

class ListUsingArray<E> implements ListInterfaces<E> {
	private static final int MAXSIZE = 1000;
	private int num_nodes = 0;
	@SuppressWarnings("FieldMayBeFinal")
	private E[] arr = (E[]) new Object[MAXSIZE];

	@Override
	public boolean isEmpty() {
		return num_nodes == 0;
	}

	@Override
	public int size() {
		return num_nodes;
	}

	@Override
	public E getFirst() throws NoSuchElementException {
		if (num_nodes == 0)
			throw new NoSuchElementException("can't get from an empty list");
		else
			return arr[0];
	}

	@Override
	public boolean contains(E item) {
		for (int i = 0; i < num_nodes; i++)
			if (arr[i].equals(item))
				return true;

		return false;
	}

	@Override
	public void addFirst(E item) throws IndexOutOfBoundsException {
		if (num_nodes == MAXSIZE)
			throw new IndexOutOfBoundsException("insufficient space for add");
		for (int i = num_nodes - 1; i >= 0; i--)
			arr[i + 1] = arr[i]; // to shift elements to the right

		arr[0] = item;
		num_nodes++; // update num_nodes
	}

	@Override
	public E removeFirst() throws NoSuchElementException {
		if (num_nodes == 0)
			throw new NoSuchElementException("can't remove from an empty list");
		else {
			E tmp = arr[0];
			for (int i = 0; i < num_nodes - 1; i++)
				arr[i] = arr[i + 1]; // to shift elements to the left
			num_nodes--; // update num_nodes
			return tmp;
		}
	}

	@Override
	public void print() {
		System.out.print("Array:[");
		for(int i =0;i<this.num_nodes;i++) {
			System.out.print(arr[i]);
			if(i!=this.num_nodes-1) System.out.print(" ");
		}
		System.out.print("]");
		System.out.println();
	}

	@Override
	public E removeLast() throws NoSuchElementException {
		// TODO Auto-generated method stub
		throw new UnsupportedOperationException("Unimplemented method 'removeLast'");
	}
}