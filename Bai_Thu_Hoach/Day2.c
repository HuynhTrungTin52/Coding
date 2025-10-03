//Name : Huynh Trung Tin
//Student's Code : 524k0033
#include <stdio.h>
#include <math.h>

int main()
{
	int n, numdigs;
	printf("Enter a number :");
	scanf("%d", &n);
	numdigs = floor(log10(n)) + 1;
	printf("The numbers of digits in your number is %d", numdigs);
	return 0;
}