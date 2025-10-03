#include <stdio.h>

int main()
{
	int n, i, sum = 0;
	printf("Enter a value for N to see if it's a perfect number :");
	scanf("%d", &n);
	for (i = 1; i < n; i++)
	{

		if (n % i == 0)
		{
			sum += i;
		}
	}
	printf("%s", sum == n ? "The number above is a perfect number" : "The number above is NOT a perfect number");

	return 0;
}