#include <stdio.h>
#include <math.h>
int sigmafunction1(int n)
{
	// 2i+1
	if (n == 1)
	{
		return 2 * n + 1;
	}
	else
		return 2 * n + 1 + sigmafunction1(n - 1);
}

float sigmafunction2(float n)
{
	// i/2
	if (n == 1)
	{
		return n / 2;
	}
	else
		return n / 2 + sigmafunction2(n - 1);
}
int factorial(int n)
{
	if (n == 1 || n == 0)
		return 1;
	return n * factorial(n - 1);
}
int sigmafunction3(int n)
{
	// i!
	if (n == 1)
	{
		return factorial(n);
		printf("%d", factorial);
	}
	else
		return factorial(n) + sigmafunction3(n - 1);
}

float sigmafunction4(float n)
{
	// sqrt(i)
	if (n == 1)
	{
		return sqrt(n);
	}
	else
		return sqrt(n) + sigmafunction1(n - 1);
}
double pinot(int n)
{
	// i!
	if (n == 1)
	{
		return factorial(n);
	}
	else
		return factorial(n) * pinot(n - 1);
}
int main()
{
	int n;
	printf("Enter n :");
	scanf("%d", &n);
	printf("%d\n", sigmafunction1(n));
	printf("%.02f\n", sigmafunction2((float)n));
	printf("%d\n", sigmafunction3(n));
	printf("%.02f\n", sigmafunction4((float)n));
	printf("%.02lf", pinot(n));

	return 0;
}