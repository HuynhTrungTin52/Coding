#include <stdio.h>

int primechecker(int n, int m)
{
	if (n == 1)
		return 0;
	if (m == 1)
		return 1;
	if (n % m == 0)
	{
		return 0;
	}
	else
		return primechecker(n, m - 1);
}
int main()
{
	int n;
	printf("Enter an integer to see if it's a prime :");
	scanf("%d", &n);
	if (primechecker(n, n - 1) == 1)
	{
		printf("This is a prime number");
	}
	else
		printf("This isn't a prime number");

	return 0;
}