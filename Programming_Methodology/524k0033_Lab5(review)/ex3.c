#include <stdio.h>

int isprime(int n)
{
	int i, counter = 0;
	for (i = 1; i <= n; i++)
	{
		if (n % i == 0)
		{
			counter++;
		}
	}

	return counter;
}
int main()
{
	int n;
	do
	{
		printf("Enter a number to see if it's a prime number or not :");
		scanf("%d", &n);
	} while (n < 2);

	if (isprime(n) > 2)
		printf("This isn't a prime number");
	else
		printf("This is a prime number");

	return 0;
}