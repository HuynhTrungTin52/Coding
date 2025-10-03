#include <stdio.h>
#include <math.h>

int ISwearIAmnotCopyingAndPastingMyOldHomework(int n)
{
	int numlen, isPalin = 1;
	int i, j, k;
	numlen = floor(log10(n)) + 1;
	for (i = 1, j = numlen, k = 0; i <= numlen; i++, j--, k++)
	{

		isPalin = isPalin * (n / (int)pow(10, j - 1) % 10 == n % (int)pow(10, i) / (int)pow(10, k));
	}

	return isPalin;
}
int main()
{
	int n;
	printf("Enter value for N :");
	scanf("%d", &n);

	switch(ISwearIAmnotCopyingAndPastingMyOldHomework(n))
	{
		case 1:
		printf("The number above is a Palindrome");
		break;
		case 0:
		printf("The number above is NOT a Palindrome");
		break;
	}

	return 0;
}