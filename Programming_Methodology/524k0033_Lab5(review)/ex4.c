#include <stdio.h>
#include <math.h>

int isarmstrong(int m)
{
	int numlen = floor(log10(m)) + 1;
	int sum = 0, x;
	while (m != 0)
	{
		x = m % 10;
		sum += pow(x, numlen);
		m = m / 10;
	}

	return sum;
}
int main()
{
	int n;
	printf("Enter a number to see if it's armstrong or not :");
	scanf("%d", &n);

	printf("%s", isarmstrong(n) == n ? "The number above is an armstrong number" : "The number above is NOT an armstrong number");

	return 0;
}