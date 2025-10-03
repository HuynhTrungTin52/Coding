#include <stdio.h>

float sigma1(int n)
{
	int i;
	float sum = 0;
	for (i = 1; i <= n; i++)
	{
		sum = sum + 1.0*i / 2;
	}
	return sum;
}

int sigma2(int n)
{
	int i, sum = 0;
	for (i = 1; i <= n; i++)
	{
		sum = sum + (2 * i + 1);
	}
	return sum;
}
float sigma3(int n)
{
	float i;
	float sum = 0;
	for (i = 1; i <= n; i++)
	{
	sum = sum + ((i+1)/(i+2));
	}
	return sum;
}
int sigma4(int n)
{
	int i, fac = 1, j, sum = 0;
	for (i = 1; i <= n; i++,fac=1)
	{
		for (j = 1; j <= i; j++)
		{
			fac *= j;
			
		}
		sum += fac + 1;
	}
	return sum;
}
int masig1(int n)
{
	int i, fac = 1;
	int prod=1;
	for (i = 1; i <= n; i++)
	{
		prod *= i ;
	}
	return prod;
}
unsigned long masig2(int n)
{
	 int i, fac = 1, j;
	unsigned long prod=1;
	for (i = 1; i <= n; i++,fac=1)
	{
		for (j = 1; j <= i; j++)
		{
			fac *= j;
			
		}
		prod *= fac;
	}
	return prod;
}
float masig3(int n)
{
	 int i, fac = 1, j; 
	 float prod=1;
	for (i = 1; i <= n; i++,fac=1)
	{
		prod *= (2.0*i)/3 ;
	}
	return prod;
}

float masig4(int n)
{
	 int fac = 1, j; 
	 float prod=1,i;
	for (i = 1; i <= n; i++)
	{
		prod = prod * ((i-1)/(i+1)) ;
	}
	return prod;
}
int main()
{
	int n;
	printf("Enter a value for N for sigmas and pi notations : ");
	scanf("%d", &n);
	printf("The first sigma(i/2) : %.2f\n", sigma1(n));
	printf("The second sigma(2i+1) : %d\n", sigma2(n));
	printf("The third sigma((i+1)/(i+2)) : %.2f\n", sigma3(n));
	printf("The fourth sigma(i!+1) : %d\n", sigma4(n));
	printf("The first pi notation(i) : %d\n", masig1(n));
	printf("The second pi notation(i!) : %lu\n", masig2(n));
	printf("The third pi notation(2i/3) : %.2f\n", masig3(n));
	printf("The fourth pi notation((i-1)(i+1)) : %.2f\n", masig4(n));
	return 0;
}