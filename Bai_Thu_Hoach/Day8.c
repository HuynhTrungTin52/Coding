//Name : Huynh Trung Tin
//Student's ID : 524k0033
#include <stdio.h>

int factorial(int);
int main()
{
	int n;
	printf("Enter a number :");
	scanf("%d", &n);
	printf("%d", factorial(n));

	return 0;
}

int factorial(int n)
{
	if (n == 1 || n == 0)
		return 1;
	return n * factorial(n - 1);
}
