#include <stdio.h>
#include <math.h>
#define pi 3.14159265359
int main()
{
	printf("Enter the radius of a circle :");
	double rad;
	scanf("%lf", &rad);
	double area=pi*pow(rad,2.0);
	printf("The area of a circle is :%.2lf",area);
	return 0;
}