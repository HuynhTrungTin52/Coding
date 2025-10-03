import java.util.Scanner;

public class Ex07 {

	public static boolean isPalin(MyStack<Character> stack, MyQueue<Character> queue) {
		for(int i =0;i<stack.size();i++) {
			if(stack.pop() != queue.deQueue()) {
				return false;
			}
		}
		return true;
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		MyStack<Character> stack = new MyStack<>();
		MyQueue<Character> queue = new MyQueue<>();
		System.out.print("Enter a string to check:");
		String str= in.nextLine();
		for(Character letter : str.toCharArray()) {
			stack.push(letter);
			queue.enQueue(letter);
		}
		if(isPalin(stack,queue)) {
			System.out.print("The string above is a palindrome");
		} else {
			System.out.print("The string above is NOT a palindrome");
		}
		in.close();
	}	
}
