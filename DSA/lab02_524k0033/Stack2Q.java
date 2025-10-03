public class Stack2Q<E> implements QueueInterface<E>{
	private MyStack<E> inbox = new MyStack<>();
	private MyStack<E> outbox = new MyStack<>();
	@Override

	public void enQueue(E item) {
		inbox.push(item);
	}
	@Override
	public E deQueue() {
		if (outbox.isEmpty()) {
            while (!inbox.isEmpty()) {
               outbox.push(inbox.pop());
            }
        }
        return outbox.pop();
	}
	@Override
	public int size() {
		return inbox.size()+outbox.size();
	}
	@Override
	public boolean contains(E item) {
		return inbox.contains(item) || outbox.contains(item);
	}
	@Override
	public void print() {
		Stack2Q<E> temp = new Stack2Q<>();
		E item;

		while(!isEmpty()) {
			item = this.deQueue();
			temp.enQueue(item);
		}
		item=temp.deQueue();
		System.out.print("List: "+item);
		this.enQueue(item);
		while(!temp.isEmpty()) {
			item =temp.deQueue();
			System.out.print(" -> ");
			System.out.print(item);
			this.enQueue(item);
		}

		
		System.out.println();
	}
	@Override
	public boolean isEmpty() {
		return inbox.isEmpty() && outbox.isEmpty();
	}
	@Override
	public E getFront() {
		if (outbox.isEmpty()) {
            while (!inbox.isEmpty()) {
               outbox.push(inbox.pop());
            }
        }
		return outbox.getPeek();
	}
	
}
