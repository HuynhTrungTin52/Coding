// Name : Huynh Trung Tin
// Student's code : 524k0033 

#include <stdio.h>
#include <math.h>


int triangle(double a, double b, double c)
{

	if ((a + b > c) && (b + c > a) && (a + c > b))
		return 1;
	else
		return 0;
}

double peri(double a, double b, double c)
{

	return (a + b + c) / 2.0;
}

double area(double a, double b, double c)
{
	double p = peri(a, b, c);
	return sqrt(p * (p - a) * (p - b) * (p - c));
}

int main()
{
	double a, b, c;

	printf("Input the following a,b,c: ");
	scanf("%lf%lf%lf", &a, &b, &c);

	if (triangle(a, b, c) == 1)
	{
		printf("This is a triangle");
		printf("\nHalf Perimeter: %.2lf", peri(a, b, c));
		printf("\nArea: %.2lf", area(a, b, c));
	}
	else
		printf("This is not a triangle!");
}
