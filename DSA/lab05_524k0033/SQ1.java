package lab05_524k0033;

import java.util.Scanner;
import java.util.Stack;

public class SQ1 {

	public static double CalculatePostfix(String str) {
		Stack<String> stack = new Stack<>();
		String[] split_str= str.split(" ");
		for(String sstr : split_str ) {
			if (sstr.equals("+") || sstr.equals("-") || sstr.equals("*") || sstr.equals("/")) {
				double a = Double.parseDouble(stack.pop());
				double b = Double.parseDouble(stack.pop());
				double res = 0;
				switch (sstr) {
					case "+": res = b + a; break;
					case "-": res = b - a; break;
					case "*": res = b * a; break;
					case "/": res = b / a; break;
				}
				stack.push(String.valueOf(res));
			} else {
				stack.push(sstr);
			}
		}
		return Double.parseDouble(stack.peek());

	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter an infix :");
		String str = in.nextLine();
		System.out.print(CalculatePostfix(str));





		in.close();

	}
}
