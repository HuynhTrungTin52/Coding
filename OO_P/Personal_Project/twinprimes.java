package Personal_Project;

public class twinprimes {
	
	public static boolean isPrime(int num)
	{
		
		for(int i=2;i<num/2;i++)
		{
			if(num%i==0) return false;
		}
	return true;
	}
	
	public static void main(String[] args) {
		long num=1000000000;
    
		for(int i=2;i<=num;i++)
		{
			if(isPrime(i) && isPrime(i+2) )
			{
					System.out.printf("%d and %d\n",i,i+2);
			}
			
		}
	}
}
