#include <stdio.h>

int main()
{
    // Exercise 2 
    int a,b;
    printf("Enter two values :");
    scanf("%d%d", &a, &b);
    printf("%d + %d = %d\n", a, b, a+b);
    printf("%d - %d = %d\n", a, b, a-b);
    printf("%d x %d = %d\n", a, b, a*b);
    printf("%d : %d = %.2f\n", a, b, 1.0*a/b);
    return 0;
}