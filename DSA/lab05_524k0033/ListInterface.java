import java.util.NoSuchElementException;

public interface ListInterface<E> {
    public void addFirst(E item);

    public void addLast(E item);


    public boolean removeAt(int position) throws NoSuchElementException;

    public void print();

    public int countOdd();

    public int searchKey(int key);

    public boolean checkSorted();

    public Node<E> getHead();

}