package lab02_524k0033;

import java.util.Scanner;

public class Ex05 {
	// Push the left side of the bracket
	// IF we encounter the right bracket, we POP the delimeter

	public static boolean isLeft(char ch) {
		return ch == '[' || ch == '(' || ch == '{';
	}

	public static boolean matched(char left, char right) {

		switch (left) {
			case '(':
				return right == ')';
			case '[':
				return right == ']';
			case '{':
				return right == '}';
		}
		return false;

	}

	public static boolean isBalanced(String seq) {
		MyStack<Character> stack = new MyStack<>();
		for (char letter : seq.toCharArray()) {
			if (isLeft(letter)) {
				stack.push(letter);
			} else {
				if (!matched(stack.pop(), letter)) {
					return false;
				}
			}
		}
		if(!stack.isEmpty()) return false;
		return true;
	}

	public static void main(String[] args) {

		Scanner in = new Scanner(System.in);
		System.out.print("Enter a set of parentheses :");
		String str = in.next();

		if(isBalanced(str)) {
			System.out.print("The above parentheses is VALID");
		} else {
			System.out.print("The above parentheses is INVALID");
		}

		in.close();

	}

}
