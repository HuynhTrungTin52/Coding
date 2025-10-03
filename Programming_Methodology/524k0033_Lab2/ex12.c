#include <stdio.h>

int main()
{
	int n, i, counter = 0;
	do
	{
		printf("Enter a number to see if it's a prime number or not :");
		scanf("%d", &n);
	} while (n < 1);
	for (i = 1; i <= n; i++)
	{
		if (n % i == 0)
		{
			counter++;
		}
	}
	if (counter > 2)
		printf("This isn't a prime number");
	else
		printf("This is a prime number");

	return 0;
}