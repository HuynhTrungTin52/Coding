#include <stdio.h>
#include <math.h>

int main()
{
	int i, j, numlen, n, k;
	char isPalin = 1;

	printf("Enter value for N :");
	scanf("%d", &n);
	numlen = floor(log10(n)) + 1;
	for (i = 1, j = numlen, k = 0; i <= numlen; i++, j--, k++)
	{
		isPalin=isPalin*((n / (int)pow(10, j - 1) % 10) == (n % (int)pow(10, i) / (int)pow(10, k)));
	}
	if (isPalin == 1)
		printf("The number above is a Palindrome");
	else
		printf("The number above is NOT a Palindrome");
	return 0;
}