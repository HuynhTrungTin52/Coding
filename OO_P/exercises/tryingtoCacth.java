import java.util.*;

class tryingtoCatch {
	public static double division(int a, int b) throws IllegalArgumentException {
		if (b==0) {
			IllegalArgumentException e = new IllegalArgumentException("Cannot divide by 0");
			throw e;
		} else return a/b;
	}
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Enter the first input :");
		int num1=in.nextInt();
		System.out.println("Enter the second input :");
		int num2=in.nextInt();
		System.out.printf("%d + %d=%.2f",num1,num2,division(num1,num2));	
	}
}