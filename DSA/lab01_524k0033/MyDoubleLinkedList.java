import java.util.NoSuchElementException;


public class MyDoubleLinkedList {
	private DoubleNode head;
    private int numNode;

    public MyDoubleLinkedList() {
        head = null;
        numNode = 0;
    }

    
    public void addFirst(double item) {
        head = new DoubleNode(item, head);
        numNode++;
    }

    
    public void addAfter(DoubleNode curr, double item) {
        if (curr == null) {
            addFirst(item);
        } else {
            DoubleNode newNode = new DoubleNode(item, curr.getNext());
            curr.setNext(newNode);
            numNode++;
        }
    }

    
    public void addLast(double item) {
        if (head == null) {
            addFirst(item);
        } else {
            DoubleNode tmp = head;
            while (tmp.getNext() != null) {
                tmp = tmp.getNext();
            }
            DoubleNode newNode = new DoubleNode(item, null);
            tmp.setNext(newNode);
            numNode++;
        }
    }

    
    public double removeFirst() throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else {
            DoubleNode tmp = head;
            head = head.getNext();
            numNode--;
            return tmp.getData();
        }
    }

    
    public double removeAfter(DoubleNode curr) throws NoSuchElementException {
        if (curr == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else {
            DoubleNode delNode = curr.getNext();
            if (delNode != null) {
                curr.setNext(delNode.getNext());
                numNode--;
                return delNode.getData();
            } else {
                throw new NoSuchElementException("No next node to remove");
            }
        }
    }

    
    public double removeLast() throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else {
            DoubleNode preNode = null;
            DoubleNode delNode = head;
            if (delNode.getNext() == null) {
                return removeFirst();
            }
            while (delNode.getNext() != null) {
                preNode = delNode;
                delNode = delNode.getNext();
            }
            preNode.setNext(delNode.getNext());
            numNode--;
            return delNode.getData();
        }
    }

    
    public double removeCurr(DoubleNode Curr) throws NoSuchElementException {
        if (Curr == null) {
            throw new NoSuchElementException("Can't remove element from an empty list");
        } else {
           DoubleNode pre=null,del=head;
           while(del!=Curr){
            pre=del;
            del.getNext();
           }
           return removeAfter(pre);
        }
    }

    public double getCurr(int index) throws NoSuchElementException {
        if(head==null) {
            throw new NoSuchElementException("Can't get an element from an empty list");
        }
        if(index>numNode) {
            throw new NoSuchElementException("Can't pick element at index bigger than size of list");
        }
        if(index==0) {
            return head.getData();
        } 
        int i=0;
        DoubleNode curr=head;
        while(i!=index) {
            i++;
            curr=curr.getNext();
        }
        return curr.getData();
    }
    
    public void print() {
        if (head != null) {
            DoubleNode tmp = head;
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

    
    public boolean isEmpty() {
        if (numNode == 0)
            return true;
        return false;
    }

    
    public double getFirst() throws NoSuchElementException {
        if (head == null) {
            throw new NoSuchElementException("Can't get element from an empty list");
        } else {
            return head.getData();
        }
    }

    
    public DoubleNode getHead() {
        return head;
    }

    public DoubleNode setHead(DoubleNode newHead) {
        DoubleNode delNode=this.head;
        this.head=newHead;
        return delNode;
    }

    
    public int size() {
        return numNode;
    }

    
    public boolean contains(double item) {
        DoubleNode tmp = head;
        while (tmp != null) {
            if (tmp.getData().equals(item))
                return true;
            tmp = tmp.getNext();
        }
        return false;
    }
}
