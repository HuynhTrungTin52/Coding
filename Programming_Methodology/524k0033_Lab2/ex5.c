#include <stdio.h>

int main()
{
    int n, numlen;
    int lastdig;
    printf("Enter value for N :");
    scanf("%d", &n);
    lastdig = n % 10;
    int firstdig = n;
    while (firstdig > 10)
    {
        firstdig /= 10;
    }

    printf("First and last digit of %d is %d and %d", n, firstdig, lastdig);

    return 0;
}