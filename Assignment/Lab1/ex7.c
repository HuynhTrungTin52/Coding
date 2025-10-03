#include <stdio.h>

int main()
{
    // Exercise 7
    int year;
    int check1, check2, check3;
    char a = 'N', b = 'O', c = ' '; 
    printf("Enter a year to see if it's leap year or not :");
    scanf("%d", &year);
    // A leap year is divisible by 4, and if it's a century then it must be divisible by 400
    check1= year % 4 ==0;
    check2= (year % 100 == 0) ? 1 : 0;
    check3= (check2 == 1) ? (year % 400 ==0) : 1;
    check1=check1*check3;
    printf("%c%c%c", a - check1*('N'-'Y'), b- check1*('O'-'E'), c- check1*(' '-'S'));
    return 0;
}