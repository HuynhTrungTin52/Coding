package lab02_524k0033;

import lab01_524k0033.Fraction;

public class TestQueue {
	public static void main(String[] args) {
		MyQueue<Fraction> queue2 = new MyQueue<>();
		for(int i =1; i<=10;i++) {
			queue2.enQueue(new Fraction(i,i+3));
			
		}
		queue2.print();
		queue2.enQueue(new Fraction(10,11));
		queue2.deQueue();
		queue2.deQueue();
		queue2.enQueue(new Fraction(11,25));
		queue2.deQueue();
		queue2.print();
		System.out.print(queue2.getFront());
	}
}
