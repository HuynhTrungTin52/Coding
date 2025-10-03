#include <stdio.h>
#include <math.h>
int main()
{
	int n, m, x, numlen, i, sum = 0;
	printf("Enter a number to see if it's armstrong or not :");
	scanf("%d", &n);
	// Armstrong numbers are sum of digits powered to the numlen = number
	numlen = floor(log10(n)) + 1;
	m = n;
	while (m != 0)
	{
		x = m % 10;
		sum += pow(x, numlen);
		m = m / 10;
	}
	printf("%s", sum == n ? "The number above is an armstrong number" : "The number above is NOT an armstrong number");

	return 0;
}