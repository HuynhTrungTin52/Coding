#include <stdio.h>

int main()
{
    // Exercise 3 
    float length, width;
    printf("Enter the length and width of the rectangle respectively :");
    scanf("%f %f", &length, &width);
    printf("So the area of a rectangle is %.2f and the perimeter of a rectangle is %.2f :", length*width, 2.0*(length+width));
    return 0;
}