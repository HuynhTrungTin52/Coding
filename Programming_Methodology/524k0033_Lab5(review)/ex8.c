#include <stdio.h>
void perfectnumber(int n)
{
	printf("Perfect numbers between 1 to %d using For Loop is :\n", n);
	int i, j, sum;
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
}
int main()
{
	int n;
	do
	{
		printf("Enter a value for N to check the Perfect numbers between 1 and N :");
		scanf("%d", &n);
	} while (n <= 1);

	perfectnumber(n);
	return 0;
}