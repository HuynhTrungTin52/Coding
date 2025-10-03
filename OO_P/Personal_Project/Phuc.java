package Personal_Project;

import java.util.Scanner;

public class Phuc {

	public static boolean isPrime(int num){
		if(num==1 || num==0) return false;
		for(int i=2;i<=Math.sqrt(num);i++)
		{
			if(num%i==0) return false;
		}
	return true;
	}
	public static int[] primeArr(int[] arr, int pCount)
	{
		int[] newArr= new int[pCount];
		for(int i=0,j=0;i<arr.length;i++){
			if(isPrime(arr[i])){
				newArr[j++]=arr[i];
				
			}
		}
	return newArr;
	}
	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)){
		int[] arr = new int[10];
		int pCount=0;
		for (int i = 0; i < 10; i++) {
			System.out.printf("Enter index %d of the array :",i);
			arr[i]=in.nextInt();
			if(isPrime(arr[i])) pCount++;
		}
		System.out.print("Your array of only prime numbers :");
		int[] newArr=primeArr(arr,pCount);
		for(int num : newArr){
			System.out.print(num + " ");
		}
		}
	}
}