package review1;

import java.util.Scanner;
public class MyArray{

	public static void assignArray(int[] arr, Scanner in){
		for(int i=0;i<arr.length;i++) {
			System.out.printf("Enter index %d of array :",i);
			arr[i]=in.nextInt();
		}
	}
	public static boolean isPrime(int n) {
		if(n==1 || n<=0) return false;
		for(int i=2;i<=Math.sqrt(n);i++) {
			if (n%i==0) return false; 
		}
	return true;
	}
	public static int[] primes(int[] candidates) {
		int length=0;
		for(int i : candidates) {
			if(isPrime(i)) length++;
		}
		int[] newArr= new int[length];
		for(int i=0,j=0;i<candidates.length;i++) {
			if(isPrime(candidates[i])) {
				newArr[j]=candidates[i];
				j++;
			}
		}
	return newArr;
	}
	public static void main(String args[]){

		Scanner in = new Scanner(System.in);
		System.out.print("Enter length of the array :");
		int length = in.nextInt();
		int[] arr = new int[length];
		assignArray(arr,in);
		int[] primeArr=primes(arr);
		for(int i : primeArr) {
			System.out.println(i);
		}
		in.close();
	}
}