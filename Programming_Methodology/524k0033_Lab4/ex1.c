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
int sigma3(int n)
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
unsigned long masig1(int n)
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
float masig2(int n)
{
	 int i, fac = 1, j; 
	 float prod=1;
	for (i = 1; i <= n; i++,fac=1)
	{
		prod *= (2.0*i)/3 ;
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
	printf("The third sigma(i!+1) : %d\n", sigma3(n));
	printf("The first pi notation(i!) : %lu\n", masig1(n));
	printf("The second pi notation(2i/3) : %.2f\n", masig2(n));

	return 0;
}