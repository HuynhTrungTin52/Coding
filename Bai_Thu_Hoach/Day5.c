//Name : Huynh Trung Tin
// Student's code : 524k0033
#include <stdio.h>
#include <math.h>

int main()
{
	int R, O[2], A[2];
	double distance;
	printf("Give me R of a circle :");
	scanf("%d", &R);
	printf("Give me X and Y of point A :");
	scanf("%d %d", A, A + 1);
	printf("Give me X and Y of the center of the circle :");
	scanf("%d %d", O, O + 1);
	distance = sqrt(pow((*A - *O), 2) + pow((*(A + 1) - *(O + 1)), 2));
	if(distance>R)
	{
		printf("Point A is outside of the circle");
	}
	if(distance<R)
	{
		printf("Point A is inside of the circle");
	}
	if(distance==R)
	{
		printf("Point A is on the line of the circle");
	}	
	return 0;
}