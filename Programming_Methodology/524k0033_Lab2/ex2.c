#include <stdio.h>

int main()
{
    int n;
    do
    {
        printf("Enter value for N :");
        scanf("%d", &n);
    } while (n < 1);
    int i = 0;
    printf("All of the odd numbers from 1 to n using Do-While loop :\n");
    do
    {
        if (++i % 2 != 0)
            printf("%d ", i);
    } while (i < n);
    printf("\nAll of the odd numbers from 1 to n using While loop :\n");
    i = 0;
    while (i <= n)
    {
        if (++i % 2 != 0)
            printf("%d ", i);
    }
    printf("\nAll of the odd numbers from 1 to n using For loop:\n");
    for (i = 1; i <= n; i++)
    {
        if (i % 2 != 0)
            printf("%d ", i);
    }

    return 0;
}