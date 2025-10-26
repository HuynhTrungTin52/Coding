package lab05_524k0033;

import java.util.NoSuchElementException;

public class IntLinkedList implements ListInterface<Integer> {
    private Node<Integer> head;
    private int numNode;

    public IntLinkedList() {
        head = null;
        numNode = 0;
    }

    @Override
    public void addFirst(Integer item) {
        head = new Node<Integer>(item, head);
        numNode++;
    }

    @Override
    public void addLast(Integer item) {
        if (head == null) {
            addFirst(item);
        } else {
            Node<Integer> tmp = head;
            while (tmp.getNext() != null) {
                tmp = tmp.getNext();
            }
            Node<Integer> newNode = new Node<Integer>(item, null);
            tmp.setNext(newNode);
            numNode++;
        }
    }

    public boolean removeFirst() throws NoSuchElementException {
        if (head == null) {
            return false;
        } else {
            head = head.getNext();
            numNode--;
            return true;
        }
    }

    public boolean removeAfter(Node<Integer> curr) throws NoSuchElementException {
        if (curr == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else {
            Node<Integer> delNode = curr.getNext();
            if (delNode != null) {
                curr.setNext(delNode.getNext());
                numNode--;
                return true;
            } else {
                throw new NoSuchElementException("No next node to remove");
            }
        }
    }

    public boolean removeLast() throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else {
            Node<Integer> preNode = null;
            Node<Integer> delNode = head;
            if (delNode.getNext() == null) {
                return removeFirst();
            }
            while (delNode.getNext() != null) {
                preNode = delNode;
                delNode = delNode.getNext();
            }
            preNode.setNext(delNode.getNext());
            numNode--;
            return true;
        }
    }

    @Override
    public boolean removeAt(int position) throws NoSuchElementException {
        if (getHead() == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else if (position == 1) {
            removeFirst();
        } else if (position <= numNode) {
            Node<Integer> pre = null, del = head;
            int i = 1;
            while (i != position) {
                pre = del;
                del = del.getNext();
                i++;
            }

            return removeAfter(pre);
        }
        return false;
    }

    @Override
    public void print() {
        if (head != null) {
            Node<Integer> tmp = head;
            System.out.print("List: " + tmp.getData());
            tmp = tmp.getNext();
            while (tmp != null) {
                System.out.print(" -> " + tmp.getData());
                tmp = tmp.getNext();
            }
            System.out.println();
        } else {
            System.out.println("List is empty!");
        }
    }




    @Override
    public Node<Integer> getHead() {
        return head;
    }




    @Override
    public int countOdd() {
        int count=0;
        for(Node<Integer> curr=head;curr!=null;curr=curr.getNext()) {
            if(curr.getData() %2 ==1) count++;
        }
        return count;
    }

    @Override
    public int searchKey(int key) {
        int i=1;
        for(Node<Integer> curr=head;curr!=null;curr=curr.getNext(),i++) {
            if(curr.getData() == key) return i;
        }
        return -1;
    }

    @Override
    public boolean checkSorted() {
        boolean ascending=true,descending=true;
        for(Node<Integer> curr=head,next = curr.getNext();next!=null;curr=curr.getNext(),next=curr.getNext()) {
            if(next.getData()>curr.getData()) {
                descending=false;
            } else ascending=false;

        }
        return ascending || descending;
    }
}