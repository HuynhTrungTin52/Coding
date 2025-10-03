#include <stdio.h>

int isperfect(int n)
{
	int sum = 0, i;
	for (i = 1; i < n; i++)
	{

		if (n % i == 0)
		{
			sum += i;
		}
	}

	return sum;
}
int main()
{
	int n;
	printf("Enter a value for N to see if it's a perfect number :");
	scanf("%d", &n);

	printf("%s", isperfect(n) == n ? "The number above is a perfect number" : "The number above is NOT a perfect number");

	return 0;
}