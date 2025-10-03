#include <stdio.h>
#include <math.h>
int main()
{
	// formula : sqrt((Xa-Xb)^2+(Ya-Yb)^2)
	double X[2], Y[2];
	printf("Enter the cordinates for the first point :");
	scanf("%lf %lf", X, Y);
	printf("Enter the cordinates for the second point :");
	scanf("%lf %lf", &X[1], &Y[1]);
	double distance = sqrt(pow((X[0] - X[1]), 2) + pow((Y[0] - Y[1]), 2));
	printf("The distance between two points is :%.02lf", distance);

	return 0;
}