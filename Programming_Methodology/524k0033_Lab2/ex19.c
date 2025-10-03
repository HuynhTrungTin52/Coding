#include <stdio.h>

int main()
{
	int n, i, fac = 1;
	do
	{
		printf("Enter a value to be factorial :");
		scanf("%d", &n);
	} while (n < 0);
	for (i = 1; i <= n; i++)
	{
		fac *= i;
	}
	printf("The factorial of your number is %d", fac);
	return 0;
}