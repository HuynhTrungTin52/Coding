package exercises;
import java.util.*;

public class  MyArrays {

    public static int findMax(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max)
                max = arr[i];
        }
        return max;
    }

    public static int firstNeg(int[] arr) {
        int i;
        for (i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                return i;
            }
        }

        return -1;
    }

    public static int sumArr(int[] arr) {
        int sum = 0;
        for (int value : arr) {
            sum += value;
        }
        return sum;
    }

    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; ++i) {
            int j = i - 1;
            int key = arr[i];
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    public static int[] addElement(int[] arr, int n) {
        int[] newArr = new int[arr.length + 1];
        newArr[0] = n;
        for (int i = 0, j = 1; i < arr.length; i++, j++) {
            newArr[j] = arr[i];
        }
        return newArr;
    }

    public static int[] delElement(int[] arr) {
        int[] newArr = new int[arr.length - 1];
        int wasteIn = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0) {
                wasteIn = i;
                break;
            }
        }
        for(int j=0,i=0;j<newArr.length;j++,i++)
        {
            if(i==wasteIn)
            {
                
                j--;
                
            }
            else newArr[j]=arr[i];
        }
    return newArr;
    }

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            System.out.print("Enter the length of an array :");
            int length = in.nextInt();
            int[] arr = new int[length];
            for (int i = 0; i < length; i++) {
                System.out.printf("Enter index %d for array :", i);
                arr[i] = in.nextInt();
            }
            System.out.println("Enter a character do perform the action on the array :");

            char choice = 'z';
            while (choice != 'q') {
                System.out.println("a. List all values of the array");
                System.out.println("b. List all negative values of the array");
                System.out.println("c. Print the max value in the index");
                System.out.println("d. Find the first negative value");
                System.out.println("e. Calculate and Print the sum of all values");
                System.out.println("f. Sort the array in an asecending order");
                System.out.println("g. Add element x to the first position of the array");
                System.out.println("h. Delete the first greater 0 element in the array");
                System.out.println("q. quit");
                choice = in.next().charAt(0);

                switch (choice) {

                    case 'a' -> {
                        for (int value : arr) {
                            System.out.println(value);
                        }
                    }
                    case 'b' -> {
                        for (int value : arr) {
                            if (value < 0) {
                                System.out.println(value);
                            }
                        }
                    }
                    case 'c' -> {
                        System.out.println("The maximum number in the array is: " + findMax(arr));
                    }
                    case 'd' -> {
                        int negIndex = firstNeg(arr);
                        if (negIndex == -1)
                            System.out.println("No negative value found");
                        else
                            System.out.println(
                                    "The first negative value is found at index " + negIndex + " : " + arr[negIndex]);
                    }
                    case 'e' -> {
                        System.out.println("The sum of the array is :" + sumArr(arr));
                    }
                    case 'f' -> {
                        insertionSort(arr);
                        for (int value : arr) {
                            System.out.print(value + " ");

                        }
                        System.out.println();
                    }
                    case 'g' -> {
                        System.out.print("Enter the value youw want to add :");
                        int n = in.nextInt();
                        arr = addElement(arr, n);
                        for (int value : arr) {
                            System.out.print(value + " ");

                        }
                        System.out.println();
                    }
                    case 'h' -> {
                        arr = delElement(arr);
                        for (int value : arr) {
                            System.out.print(value + " ");

                        }
                        System.out.println();
                    }
                    default -> {
                        return;
                    }
                }
            }
        }
    }

}
