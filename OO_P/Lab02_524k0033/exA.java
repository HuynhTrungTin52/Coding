// package Lab02_524k0033;

// import java.util.Scanner;

// public class exA {
// 	public static boolean isPrime(int n) {
// 		if (n < 0 || n == 1)
// 			return false;
// 		for (int i = 2; i <= Math.sqrt(n); i++) {
// 			if (n % i == 0)
// 				return false;
// 		}
// 		return true;
// 	}

// 	public static void assignArray(int[] arr, Scanner in) {

// 		for (int i = 0; i < arr.length; i++) {
// 			System.out.printf("Enter array[%d] :", i);
// 			arr[i] = in.nextInt();
// 		}

// 	}

// 	public static int findMax(int[] arr) {
// 		int max = 0;
// 		for (int num : arr) {
// 			max = num > max ? num : max;

// 		}
// 		return max;
// 	}

// 	public static int sumAllEven(int[] arr) {
// 		int total = 0;
// 		for (int num : arr) {
// 			if (num % 2 == 0)
// 				total += num;
// 		}
// 		return total;
// 	}

// 	public static int primeCount(int[] arr) {
// 		int count = 0;
// 		for (int num : arr) {
// 			if (isPrime(num))
// 				count++;
// 		}
// 		return count;
// 	}

// 	public static int findKey(int[] arr, int key) {
// 		for (int i = 0; i < arr.length; i++) {
// 			if (key == arr[i])
// 				return i;
// 		}
// 		return -1;
// 	}

// 	public static int[] sArr(int[] arr) {
// 		int[] sArr = new int[arr.length];
// 		for (int i = 0; i < arr.length; i++) {
// 			sArr[i] = arr[i] * arr[i];
// 		}
// 		return sArr;
// 	}

// 	public static int divCount(int[] arr, int key) {
// 		int count = 0;
// 		for (int num : arr) {
// 			if (num % key == 0)
// 				count++;
// 		}
// 		return count;
// 	}

// 	public static int thirdLarg(int[] arr) {
// 		int max2 = 0, max3 = 0;
// 		int max1 = findMax(arr);
// 		for (int num : arr) {
// 			max2 = num > max2 && num != max1 ? num : max2;
// 		}
// 		for (int num : arr) {
// 			max3 = num > max3 && num != max2 && num != max1 ? num : max3;
// 		}
// 		return max3;
// 	}

// 	public static int[] removeKey(int[] arr, int key) {
// 		int[] newArr = new int[arr.length - 1];
// 		for (int i = 0, j = 0; j < newArr.length; i++) {
// 			if (arr[i] != key) {
// 				newArr[j] = arr[i];
// 				j++;
// 			}
// 		}
// 		return newArr;
// 	}

// 	public static int[] insertKey (int[] arr,int key, int index)
// 	{
// 		int[] newArr = new int[arr.length];
// 		for(int i=0,j=0;j<arr.length;j++){
			
// 			if(i==index && i ==j){
// 			newArr[j]=key;
			
// 			}
// 			else {newArr[j]=arr[i]; i++;}
			
// 		}
// 		return newArr;
// 	}
// 	public static void printDupes(int[] arr)
// 	{
// 		int[] dupeArr= new int[arr.length];
// 		for(int i=0;i<arr.length;i++){
// 			for(int j=i+1;j<arr.length;j++){
// 				if(arr[i]==arr[j]){
// 					System
// 				}
// 			}
// 		}
		
// 	}
// 	public static int[] remove_index(int[] arr, int remover)
// 	{
// 		int[] newArr = new int[arr.length-1];
// 		for(int i=0,j=0;i<arr.length;i++)
// 		{
// 			if(i!=remover)
// 			{
// 			newArr[j]=arr[i];
// 			j++;
// 		}
		 
// 		}
// 	return newArr;
// 	}
// 	public static int[] eraseDupes(int[] arr)
// 	{
// 		int count =0;
// 		for(int i=0;i<arr.length;i++){
// 			for(int j=i+1;j<arr.length;j++){
// 				if(arr[i]==arr[j]){ count++; break;}
// 			}
// 		}
// 		int[] newArr = new int[arr.length-count];
// 		for(int i=0;i<arr.length;i++)
// 		{
// 			for(int k=i+1;k<arr.length;k++)
// 			{
// 				if(arr[i]==arr[k])
// 				 arr=remove_index(arr, k);
// 			}	
// 		}
// 	for(int i=0;i<newArr.length;i++){newArr[i]=arr[i];}
// 	return newArr;
// 	}

// 	Unfinished
// 	public static void main(String[] args) {
// 		try (Scanner in = new Scanner(System.in)) {
// 			System.out.print("Enter the length of the array :");
// 			int length = in.nextInt();
// 			int[] arr = new int[length];
// 			assignArray(arr, in);
// 			 System.out.println("The Maximum Value in the array is :" + findMax(arr));  Assignment 1
// 			 System.out.println("The sum of all even number in the array is :" + sumAllEven(arr));  Assignment 2
// 			 System.out.println("The number of prime in the array is :" + primeCount(arr));  Assignment 3
// 			 System.out.print("Input a number to find in the array :");
// 			 int key = in.nextInt();
// 			 if (findKey(arr, key) != -1) {
// 			 	System.out.printf("Found your number at index %d of the array\n", findKey(arr, key));
// 			 } else
// 			 	System.out.println("Can't find your number");  Assignment 4
// 			 System.out.print("Here is your array but squared :");
// 			 int[] sArr = sArr(arr);
// 			 for (int num : sArr) {
// 			 	System.out.print(num + " ");
// 			 }  Assignment 5
// 			 System.out.printf("\nInput a number to see how many numbers in the array are divisible by it :");
// 			 key = in.nextInt();
// 			 System.out.printf("The number of numbers in the array divisble by %d is %d\n", key, divCount(arr, key)); Assignment
// 			 																										 6
// 			 System.out.println("The third largest number in the array is :" + thirdLarg(arr)); Assignment 7
// 			 System.out.print("Input a number to remove it from the element :");
// 			 key = in.nextInt();
// 			 if (findKey(arr, key) == -1) {
// 			 	System.out.println("Can't find your number");
// 			 } else {
// 			 	arr = removeKey(arr, key);
// 			 	System.out.println("Here is your new array :");
// 			 	for (int num : arr) {
// 			 		System.out.print(num + " ");
// 			 	}
// 			 }  Assignment 8
// 			 System.out.println("Input a number and the position to insert it too :");
// 			 key = in.nextInt();
// 			 int index = in.nextInt();
// 			 if (index > arr.length || index < 0)
// 			 	System.out.println("Invalid position");
// 			 else {
// 			 	arr = insertKey(arr, key, index);
// 			 	System.out.println("Here is your new array :");
// 			 	for (int num : arr) {
// 			 		System.out.print(num + " ");Assignment 9
// 			 	}

// 			 }
// 		System.out.printf("\nHere are the duplicate numbers in your array :");
// 		printDupes(arr);Assignment 10
// 		 System.out.printf("\n Erasing an element :");
// 		 arr=eraseDupes(arr);
// 		 System.out.println("Here is your new array :");
// 		 		for (int num : arr) {
// 		 			System.out.print(num + " ");Assignment 9
// 		 		}
// 		}

// 	}
// }
