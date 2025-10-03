#include <stdio.h>
#include <math.h>

int main()
{
	int n, x, y = 0, i = 0;
	printf("Enter a decimal number to change it to a binary :");
	scanf("%d", &n);
	while (n != 0)
	{
		x = n % 2;
		y = x * (int)pow(10, i++) + y;
		n /= 2;
	}
	printf("%d", y);
	return 0;
}