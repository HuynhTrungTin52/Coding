import java.util.*;


public class TestStack {

	public static String ReverseString(String str) {
		Stack<Character> list = new Stack<>();
		for(int i =0;i<str.length();i++) {
			list.push(str.charAt(i));
		}
		String res= new String("");
		while(!list.isEmpty()) {
			res+=list.pop();
		}
		return res;
	}
	public static void main (String[] args) {
		String str = new String("1234567");

		String revStr=ReverseString(str);
		System.out.print(revStr);
	}
}
