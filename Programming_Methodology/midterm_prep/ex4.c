// Name : Huynh Trung Tin
// Student's ID : 524k0033
#include <math.h>
#include <stdio.h>

int istri(float *sides)
{	
	if((sides[0]+sides[1]>sides[2]) && (sides[0]+sides[2]>sides[1]) && (sides[1]+sides[2]>sides[0]))
	{
		return 1;
	} else return 0;

}
float arify(float *sides)
{
	float p=(sides[0]+sides[1]+sides[2])/2;
	float s=sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]));
	return s;
}
int typeoftri(float *sides)
{
	if(sides[0]==sides[1] && sides[0]==sides[2] && sides[1]==sides[2])
	{
		return 1;
	}
	else if(sides[0]==sides[1] || sides[0]==sides[2] || sides[1]==sides[2])
	{
		return 2;
	} else return 0;
}
int main()
{
	float sides[3];
	printf("Enter the sides of a triangle :");
	scanf("%f %f %f", sides,sides+1,sides+2);
	if(istri(sides)==0)
	{
		printf("Error : The sides doesn't make up a triangle, ending the program");
		return 0;
	}
	float perimeter=sides[0]+sides[1]+sides[2];
	float area=arify(sides);
	printf("Perimeter of the triangle above is %.2lf and the area of the triangle is %.2f\n", perimeter,area);

	switch (typeoftri(sides))
	{
		case 0: 
		printf("This is a normal triangle");
		break;
		case 1:
		printf("This is a balanced triangle");
		break;
		case 2:
		printf("This is an isosceles triangle");
		break;
	}
	return 0;
}