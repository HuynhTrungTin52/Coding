#include <stdio.h>

int main()
{
	int num, i, prod = 1, rem;
	printf("Enter a number :");
	scanf("%d", &num);
	int x = num;
	while (x != 0)
	{
		rem = x % 10;
		prod = prod * rem;
		x = x / 10;
	}

	printf("\nProduct of the number above is :%d", prod);

	return 0;
}