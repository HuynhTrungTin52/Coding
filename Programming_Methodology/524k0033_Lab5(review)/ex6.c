#include <stdio.h>
void primenumerprint(int n)
{
	int i, j, counter = 0;
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
}
int main()
{
	int n;
	do
	{
		printf("Enter a value for N to check the prime numbers between 1 and N :");
		scanf("%d", &n);
	} while (n <= 1);

	printf("Prime numbers between 1 to %d using For Loop is :\n", n);
	primenumerprint(n);
	return 0;
}