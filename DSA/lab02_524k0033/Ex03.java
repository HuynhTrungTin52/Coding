package lab02_524k0033;

import java.util.*;

public class Ex03 {
	public static void main(String[] args) {
		MyStack<Integer> stack = new MyStack<>();
		Scanner in = new Scanner(System.in);
		System.out.print("Enter n :");
		int n= in.nextInt();
		int res=0;
		
		for(int i=n;i>0;i--) {
			if(i==1) {
				stack.push(3);
				break;
			}
			stack.push((int) Math.pow(2,i)+i*i);
			
		}
		while(!stack.isEmpty()) {
			res+=stack.pop();
		}
		System.out.print(res);
		in.close();
	}
}
