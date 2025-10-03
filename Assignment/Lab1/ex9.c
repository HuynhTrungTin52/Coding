#include <stdio.h>

int main()
{
    // Exercise 9
	int x,y,z,maxer;
    printf("Input three values to find the max number :");
    scanf("%d%d%d", &x, &y, &z);
    maxer= (x>y) ? x : y;
    maxer= (maxer>z) ? maxer : z;
    printf("The biggest number is :%d",maxer);
    return 0;
}