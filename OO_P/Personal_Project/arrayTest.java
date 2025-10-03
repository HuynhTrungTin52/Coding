package Personal_Project;
import java.util.Arrays;
public class arrayTest {

	public static int assignArray(int[] arr)
	{
		
		for(int i=0;i<arr.length;i++)
		{
			arr[i]=i;
			
		}
		return 1;
	}

	public static int[] oddOnly(int[] arr)
	{
		int[] tempArr = new int[arr.length];
		int rLength=0;
		for(int i=0;i<arr.length;i++)
		{
			if(arr[i]%2!=0)
			{
				tempArr[rLength]=arr[i];
				rLength++;
			}
		}
		 int[] newArr= Arrays.copyOf(tempArr,rLength);
		return newArr;
		} 
	public static void main(String[] args) {

		int[] arr = new int[10];
		//0 1 2 3 4 5 6 7 8 9
		//integer : -2bil -> 2bil
		//1 2 3 44, ko co 1.2
		int test =assignArray(arr);
		System.out.print(test);
		arr=oddOnly(arr);
		for(int element : arr)
		{
			
			System.out.println(element);
		}
	}
}
