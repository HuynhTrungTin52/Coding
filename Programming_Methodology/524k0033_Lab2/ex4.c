#include <stdio.h>

int main()
{
    int n, i = 0;
    int sum1 = 0, sum2 = 0, sum3 = 0;
    do
    {
        printf("Enter value for N :");
        scanf("%d", &n);
    } while (n < 1);

    do
    {
        if (++i >= 0)
            sum1 += i;
    } while (i < n);
    printf("Sum of the natural numbers from 1 to N Do-While loop is :%d", sum1);
    i = 0;
    while (i < n)
    {
        if (++i >= 0)
            sum2 += i;
    }
    printf("\nSum of the natural numbers from 1 to N While loop :%d", sum2);
    for (i = 0; i <= n; i++)
    {
        if (i >= 0)
            sum3 += i;
    }
    printf("\nSum of the natural numbers from 1 to N For loop:%d", sum3);
    return 0;
}