package lab02_524k0033;

import java.util.*;

public class Ex04 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		MyStack<Character> stack= new MyStack<>(); 
		System.out.print("Enter a string:");
		String str = in.nextLine();
		for(char letter : str.toCharArray()) {
			stack.push(letter);
		}
		String revString="";
		while(!stack.isEmpty()) {
			revString+=stack.pop();
		}
		System.out.print("Reverse string above is: " + revString);


		in.close();
	}
}
