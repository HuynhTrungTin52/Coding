#include <stdio.h>
#include <math.h>

int dec_to_bin(int n)
{
	int x, y = 0, i = 0;
	while (n != 0)
	{
		x = n % 2;
		y = x * (int)pow(10, i++) + y;
		n /= 2;
	}

	return y;
}
int main()
{
	int n;
	printf("Enter a decimal number to change it to a binary :");
	scanf("%d", &n);

	printf("%d", dec_to_bin(n));
	return 0;
}