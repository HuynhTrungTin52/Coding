#include <stdio.h>

int main()
{
    // Exercise 5
    float cel;
    printf("Enter Celcius degree to get a Farenheit degree :");
    scanf("%f", &cel);
    printf("%.2f Celcius degree is %.2f Farenheit degree", cel, (cel*9/5)+32);
    return 0;
}