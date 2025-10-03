package Lab01_524k0033;

import java.util.Scanner;
public class ex8 {
	public static int exA(int n){
		if (n==1) return 1;
		return n+exA(n-1);
	}
	public static int exB(int n){
		if (n==1) return 1;
		return n*exB(n-1);
	}
	public static long exC(int n){
		if(n==0) return (long)Math.pow(2, n);
		return (long)Math.pow(2,n)+exC(n-1);
	}
	public static double exD(int n){
		if(n==1) return 1.0/2;
		return 1.0/(2*n)+exD((n-1));
	}
	public static long exE(int n){
		if(n==1) return (long)Math.pow(n,2);
		return (long)Math.pow(n,2)+exE(n-1);
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
			System.out.print("Enter n:");
			int n = in.nextInt();
			System.out.println("Exercise A :"+exA(n));
			System.out.println("Exercise B :"+exB(n));
			System.out.println("Exercise C :"+exC(n));
			System.out.printf("Exercise D :%.3f\n",exD(n));
			System.out.print("Exercise E :" +exE(n));
			
		}
	}
}
