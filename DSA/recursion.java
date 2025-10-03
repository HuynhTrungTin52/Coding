public class recursion {

	public static void display(int n) {
		if(n>=1) {
			display(n-1);	
			System.out.print(n+" ");
		}
	}
	public static void main(String[] args) {
		display(100);		
	}	
}
