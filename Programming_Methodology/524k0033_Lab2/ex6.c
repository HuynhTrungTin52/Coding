#include <stdio.h>

int main()
{
	int num, i, sum = 0, rem;
	printf("Enter a number :");
	scanf("%d", &num);
	int x = num;
	while (x != 0)
	{
		rem = x % 10;
		sum = sum + rem;
		x = x / 10;
	}

	printf("\nSum of the number above is :%d", sum);

	return 0;
}