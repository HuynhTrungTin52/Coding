package Lab4_524k0033;

import java.util.Scanner;

public class MyArray {
	public static int maxEven(int[] arr) {
		int maxEvenat = -1;
		boolean startCheck = false;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] % 2 == 0 && startCheck == false) {
				maxEvenat = i;
				startCheck = true;
				continue;
			}
			if (startCheck == true) {
				if (arr[i] % 2 == 0 && arr[i] > arr[maxEvenat]) {
					maxEvenat = i;
				}
			}
		}
		return maxEvenat;

	}

	public static int[] input(Scanner in,int length) {
		int[] arr = new int[length];
		for (int i = 0; i < arr.length; i++) {
			System.out.printf("Enter array[%d] :", i);
			arr[i] = in.nextInt();
		}
		return arr;
	}

	public static int minOdd(int[] arr) {
		int minOddat = -1;
		boolean startCheck = false;
		for (int i = 0; i < arr.length; i++) {
			if (arr[i] % 2 != 0 && startCheck == false) {
				minOddat = i;
				startCheck = true;
				continue;
			}
			if (startCheck == true) {
				if (arr[i] % 2 == 0 && arr[i] < arr[minOddat]) {
					minOddat = i;
				}
			}
		}
		return minOddat;

	}
	public static int sumMEMO(int[] arr){
		return arr[minOdd(arr)] + arr[maxEven(arr)];
	}
	public static int sumEven(int[] arr){
		int sum=0;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]%2==0) {
				sum+=arr[i];
			}
		}
	return sum;
	}
	public static int prodOdd(int[] arr){
		int prod=1;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]%2!=0) {
				prod*=arr[i];
			}
		}
	return prod;
	}

	public static int idxFirstEven(int[] arr) {
		
		for(int i=0;i<arr.length;i++) {
			if(arr[i]%2==0) {
				return i;
			}
		}
		return -1;
	}

	public static int idxLastOdd(int[] arr) {
		int index=-1;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]%2!=0) {
				index=i;
			}
		}
		return index;
	}

	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {
			
			System.out.print("Enter the size of the array :");
			int length = in.nextInt();
			int[] arr = input(in,length);
			int temp = maxEven(arr);
			boolean noEven=false;
			boolean noOdd=false;
			if (temp == -1) {
				System.out.println("There is no even value in your array");
				noEven=true;
			} else {
				System.out.println("The greatest even number is :" + arr[temp]);
				
			}
			temp = minOdd(arr);
			if (temp == -1) {
				System.out.println("There is no odd value in your array");
				noOdd=true;
			} else
				System.out.println("The smallest odd number is :" + arr[temp]);

			if(noEven || noOdd) {
				System.out.println("There is no even or odd value in your array");
			}else
				System.out.println("The sum of max even number and min odd number is :"+ sumMEMO(arr));
			if(noEven==true){
				System.out.println("There is no even value in your array");
			} else 
				System.out.println("The sum of all even numbers is :" +sumEven(arr));
			if(noOdd==true){
				System.out.println("There is no odd value in your array");
			}else
				System.out.println("The product of all sum in the array is :"+prodOdd(arr));
			if(noEven==true){
				System.out.println("There is no even value in your array");
			}else 
				System.out.println("The first even array in your array is at index "+idxFirstEven(arr));
			if(noOdd==true){
				System.out.println("There is no odd value in your array");
			}else 
				System.out.println("The last odd number in your array is at index :" +idxLastOdd(arr));	
		}
	}
}
