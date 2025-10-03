#include <stdio.h>

int twopowered(int n)
{
	if (n == 1)
	{
		return 2;
	}
	else
		return 2 * twopowered(n - 1);
}
int main()
{
	int n;
	printf("Enter a number :");
	scanf("%d", &n);
	printf("%d", twopowered(n));

	return 0;
}