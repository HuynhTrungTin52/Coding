#include <stdio.h>
#include <math.h>

int main()
{
    int x, numlen, lastdig, y;
    printf("Enter value for N :");
    scanf("%d", &x);
    lastdig = x % 10;
    int firstdig = x;
    while (firstdig >= 10)
    {
        firstdig /= 10;
    }
    numlen = floor(log10(x)) + 1;
    printf("%d %d %d ", firstdig, lastdig, numlen);
    y = x % (int)pow(10, numlen - 1) + lastdig * pow(10, numlen - 1) - lastdig + firstdig;

    printf("The number with the first and last digit swapped is : %d", y);

    return 0;
}