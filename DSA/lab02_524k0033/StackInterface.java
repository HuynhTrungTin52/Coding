package lab02_524k0033;

import java.util.EmptyStackException;

public interface StackInterface<E> {

	public void push(E item);
	
	public E pop() throws EmptyStackException;

	public int size();

	public boolean contains(E item);

	public void print();
	
	public boolean isEmpty();

	public E getPeek();
} 