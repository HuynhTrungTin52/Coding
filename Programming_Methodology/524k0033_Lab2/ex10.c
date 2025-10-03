#include <stdio.h>
#include <math.h>

int main()
{
    int n, numlen;
    char isNega = 0;
    // 0 : False, 1 : True
    printf("Enter value for N :");
    scanf("%d", &n);
    if (n < 0)
    {
        isNega = 1;
        n *= -1;
    }
    int i = 1, j = 0;
    numlen = floor(log10(n)) + 1 < 0 ? 1 : floor(log10(n)) + 1;
    // To prevent the number overflowing if the input is zero
    printf("Your number in reverse :");
    if (isNega == 1)
        printf("-");
    while (i <= numlen)
    {
        printf("%d", n % (int)pow(10, i++) / (int)pow(10, j++));
    }

    return 0;
}