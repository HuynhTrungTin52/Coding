#include <stdio.h>
#include <math.h>

int main()
{
	int n, m, i, x, numlen, sum = 0;
	do
	{
		printf("Enter a value for N to check the Armstrong numbers between 1 and N using 3 loop structures:");
		scanf("%d", &n);
	} while (n <= 1);
	m = n;

	printf("Armstrong numbers between 1 to %d using For Loop is : \t", n);
	for (i = 1; i <= n; i++)
	{
		sum = 0;
		numlen = floor(log10(i)) + 1;
		m = i;
		while (m != 0)
		{
			x = m % 10;
			sum += (int)pow(x, numlen);
			m = m / 10;
		}
		if (sum == i)
			printf("%d ", i);
	}

	printf("\nArmstrong numbers between 1 to %d using While Loop is :\t", n);
	i = 1;
	while (i <= n)
	{
		sum = 0;
		numlen = floor(log10(i)) + 1;
		m = i;
		while (m != 0)
		{
			x = m % 10;
			sum += (int)pow(x, numlen);
			m = m / 10;
		}
		if (sum == i)
			printf("%d ", i);
		i++;
	}
	printf("\nArmstrong numbers between 1 to %d using Do-While Loop is :\t", n);
	i = 1;
	do
	{
		sum = 0;
		numlen = floor(log10(i)) + 1;
		m = i;
		while (m != 0)
		{
			x = m % 10;
			sum += (int)pow(x, numlen);
			m = m / 10;
		}
		if (sum == i)
			printf("%d ", i);
		i++;
	} while (i <= n);

	return 0;
}