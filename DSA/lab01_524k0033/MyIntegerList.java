package lab01_524k0033;

import java.util.NoSuchElementException;

public class MyIntegerList {

    public static void addBeforeEven(MyLinkedList<Integer> list,int x) {
        if(!list.isEmpty()) {
            Node<Integer> curr=list.getHead();
            if(curr.getData()%2==0) {
                list.addFirst(x);
            }

            Node<Integer> pre=null;
            while(curr!=null&&curr.getData()!=0) {
                pre=curr;
                curr=curr.getNext();
            }
            if(curr!=null) {
                list.addAfter(pre, x);
            }
        }
        
    }

    
    public static int evenSize(MyLinkedList<Integer> list) {
        int size=0;
        for(Node<Integer> n=list.getHead(); n!=null;n=n.getNext()) {
            if(n.getData()%2==0) {
                size++;
            }
        }
        return size;
    }

    
    public static int max(MyLinkedList<Integer> list) throws NoSuchElementException {
        if(list.isEmpty()) {
            throw new NoSuchElementException("Can't find maximum number in an empty list");
        }
        
        int max=list.getFirst();
        if(list.size()==1) return max;
        for(Node<Integer> n=list.getHead();n!=null;n.getNext()) {
            if(n.getData()>max) {
                max=n.getData();
            }
        }
        return max;
    }

    private static boolean isPrime(int x) {
        if(x<=1) return false;

        for(int i=2;i<= Math.sqrt(x);i++) {
            if(x%i==0) {
                return false;
            }
        }
    return true;
    }
    public static int primeSize(MyLinkedList<Integer> list) {
        int size=0;
        for(Node<Integer> n=list.getHead(); n!=null;n.getNext()) {
            if(isPrime(n.getData())) {
                size++;
            }
        }
        return size;
    }

    
    public static Node<Integer> reverseList(MyLinkedList<Integer> list) {
        Node<Integer> curr=list.getHead(),pre=null,next=null;
        while(curr!=null) {
            
            next=curr.getNext();
            curr.setNext(pre);

            pre=curr;
            curr=next;
        }
        return pre;
    }

    
    public static void sortAs(MyLinkedList<Integer> list) {
        Node<Integer> curr=list.getHead();
        while(curr!=null) {
            Node<Integer> min=curr,index=curr.getNext();

            while(index!=null) {
                if(index.getData()<min.getData()) {
                    min=index;
                }
                index=index.getNext();
            }
        int temp=curr.getData();
        curr.setData(min.getData());
        min.setData(temp);

        curr=curr.getNext();
        }

    }
    
}
