public class TestStack {
	public static void main(String[] args) {
		MyStack<Fraction> stack = new MyStack<>();
		for(int i=1;i<=10;i++) {
			stack.push(new Fraction(i,i*2+1));
		}
		stack.print();
	}
}
