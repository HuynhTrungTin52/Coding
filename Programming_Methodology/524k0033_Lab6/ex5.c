#include <stdio.h>

int digitcounter(int);
int main()
{
	int n;
	int counter = 1, *pcounter = &counter;
	printf("Enter a number :");
	scanf("%d", &n);
	printf("The number of digits is = %d", digitcounter(n));

	return 0;
}

int digitcounter(int n)
{
	if (n < 10)
	{
		return 1;
	}
	else
	{

		return 1 + digitcounter(n / 10);
	}
}