#include <stdio.h>
#include <math.h>

int calcRecursive(int n)
{
	if (n <= 1)
		return 1;
	else if (n >= 1)
	{

		return n * calcRecursive(n - 1);
	}
}
int main()
{
	int n;
	printf("Enter n :");
	scanf("%d", &n);
	printf("%d", calcRecursive(n));

	return 0;
}