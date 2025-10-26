package lab05_524k0033;
import java.util.Scanner;
import java.util.Stack;



public class SQ3 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Enter a sentence: ");
		String sentence = in.nextLine();

		String[] words = sentence.split(" ");
		Stack<String> stack = new Stack<>();

		for (String word : words) {
			stack.push(word);
		}
		String res="";
		while (!stack.isEmpty()) {
			res+=stack.pop();
			if (!stack.isEmpty()) {
				res+=" ";
			}
		}
		System.out.print(res);

		in.close();
	}
}
