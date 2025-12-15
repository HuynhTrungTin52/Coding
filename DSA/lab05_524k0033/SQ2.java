package lab05_524k0033;

import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;



public class SQ2 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a positive integer: ");
		int n = in.nextInt();
		String numStr = Integer.toString(n);

		Stack<Character> stack = new Stack<>();
		Queue<Character> queue = new LinkedList<>();

		for (char c : numStr.toCharArray()) {
			stack.push(c);
			queue.add(c);
		}

		boolean isPalindrome = true;
		while (!stack.isEmpty()) {
			if (stack.pop() != queue.remove()) {
				isPalindrome = false;
				break;
			}
		}

		if (isPalindrome) {
			System.out.println(n + " is a palindrome.");
		} else {
			System.out.println(n + " is not a palindrome.");
		}


		in.close();
	}
}
