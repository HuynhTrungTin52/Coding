#include <stdio.h>

#include <math.h>

void printarmstrong(int n)
{
	int sum = 0, numlen, m, i, x;

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
}
int main()
{
	int n;
	do
	{
		printf("Enter a value for N to check the Armstrong numbers between 1 and N :");
		scanf("%d", &n);
	} while (n <= 1);

	printf("Armstrong numbers between 1 to %d using For Loop is : \n", n);
	printarmstrong(n);

	return 0;
}