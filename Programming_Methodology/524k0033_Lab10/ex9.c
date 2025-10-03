#include <stdio.h>
#include <math.h>

int calcRecursive(int n)
{
	if (n == 0 )
		return 3;
	else if (n == 1)
	{

		return 5;
	} else return calcRecursive(n-1)+2*calcRecursive(n-2);
}
int main()
{
	int n;
	printf("Enter n :");
	scanf("%d", &n);
	printf("%d", calcRecursive(n));

	return 0;
}