#include <stdio.h>
#include <math.h>

int sigmaA(int n, int i, int sum)
{
	// n=3
	// 2*1+1 + 2*2+1 + 2*3+1
	// 2*i+1 + 2*i+1 + 2*i+1
	//
	if (i == n)
	{

		return 2*i+1;
	}
	else
	{
		sum=2*i+1;//3
		return sum + sigmaA(n,++i,sum);
		//	   3   + 5 + 7
	}
}

int factorial(int num)
{
	if(num==1)
	{
		return 1;
	} else if(num>1)
	{
		return num*factorial(num-1);
	}

}
int sigmaB(int n, int i, int sum)
{
	if(i==n)
	{
		return factorial(i)+1;
	} else 
	{
		sum=factorial(i)+1;
	} return sum +sigmaB(n,++i,sum);
}
float sigmaC(int n, int i)
{
	if (i == n)
	{

		return (2.0*i+1)/i;
	}
	else
	{
		return (2.0*i+1)/i + sigmaC(n,++i);
		
	}
}

int main()
{
	int n;
	printf("Enter n :");
	scanf("%d", &n);
	// a.2i+1
	int i = 1, sum = 0;
	printf("Sigma of 2i+1 :%d\n", sigmaA(n, i, sum));
	printf("Sigma of i!+1 :%d\n", sigmaB(n, i, sum));
	printf("Sigma of (2i+1)/i :%.1f", sigmaC(n, i));
	return 0;
}