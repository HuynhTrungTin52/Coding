#include <stdio.h>
#include <math.h>
int dec2bin(int num, int result, int i)
{

	if (num < 1)
		return result;
	int temp = (num % 2);
	result = temp * (int)pow(10, i) + result;
	return dec2bin(num / 2, result, i + 1);
}
int main()
{
	printf("Enter a positive integer :");
	int num, result = 0, i = 0;
	scanf("%d", &num);
	int bin = dec2bin(num, result, i);
	printf("%d", bin);
	return 0;
}
