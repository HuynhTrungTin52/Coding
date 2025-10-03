#include <stdio.h>

int main()
{
	int n, i, j, counter;
	do
	{
		printf("Enter a value for N to check the prime numbers between 1 and N using 3 loop structures:");
		scanf("%d", &n);
	} while (n <= 1);

	printf("Prime numbers between 1 to %d using For Loop is :\t", n);
	for (i = 1; i <= n; i++)
	{
		counter = 0;
		for (j = 1; j <= i; j++)
		{
			if (i % j == 0)
			{
				counter++;
			}
		}
		if (counter == 2)
			printf("%d ", i);
	}

	printf("\nPrime numbers betweeen 1 to %d using While Loop is :\t", n);
	i = 1;

	while (i <= n)
	{
		j = 1;
		counter = 0;
		while (j <= i)
		{
			if (i % j++ == 0)
				counter++;
		}

		if (counter == 2)
			printf("%d ", i);
		i++;
	}
	printf("\nPrime numbers betweeen 1 to %d using Do-While Loop is :\t", n);
	i = 1;

	do
	{
		j = 1;
		counter = 0;
		do
		{
			if (i % j++ == 0)
				counter++;
		} while (j <= i);

		if (counter == 2)
			printf("%d ", i);
		i++;

	} while (i <= n);

	return 0;
}