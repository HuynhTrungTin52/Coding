package lab02_524k0033;

public class MyQueue<E> extends MyLinkedList<E> implements QueueInterface<E>{

		private Node<E> front=head;
		private Node<E> rear;
		@Override
		public void enQueue(E item) {
			Node<E> newNode = new Node<>(item);
			rear =newNode;
			addLast(item);
			
		}

		@Override
		public E deQueue() {
			return removeFirst();
		}

		@Override
		public E getFront() {
			return getFirst();
		}
		
		public E getBack() {
			return rear.getData();
		}
	}
