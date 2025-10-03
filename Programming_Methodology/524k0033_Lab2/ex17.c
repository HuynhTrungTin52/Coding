#include <stdio.h>

int main()
{
	int n, i, j, sum;
	do
	{
		printf("Enter a value for N to check the Perfect numbers between 1 and N using 3 loop structures:");
		scanf("%d", &n);
	} while (n <= 1);

	printf("Perfect numbers between 1 to %d using For Loop is :  \t", n);
	for (i = 1; i <= n; i++)
	{
		sum = 0;
		for (j = 1; j < i; j++)
		{
			if (i % j == 0)
			{
				sum += j;
			}
		}
		if (sum == i)
		{
			printf("%d ", i);
		}
	}

	printf("\nPerfect numbers betweeen 1 to %d using While Loop is :\t", n);
	i = 1;
	while (i <= n)
	{
		j = 1;
		sum = 0;
		while (j < i)
		{
			if (i % j == 0)
				sum += j;
			j++;
		}

		if (sum == i)
			printf("%d ", i);
		i++;
	}
	printf("\nPerfect numbers betweeen 1 to %d using Do-While Loop is :\t", n);
	i = 1;
	do
	{
		j = 1;
		sum = 0;
		while (j < i)
		{
			if (i % j == 0)
				sum += j;
			j++;
		}

		if (sum == i)
			printf("%d ", i);
		i++;
	} while (i <= n);

	return 0;
}