#include <stdio.h>

int main()
{
    // Exercise 4
    int days, years, weeks, remDay;
    printf("Enter the specified days :");
    scanf("%d", &days);
    // years = 365 days
    // weeks = 7 days
    // years = days/365
    // weeks = days/7

    years = days/365;
    remDay= days - (365*years);
    weeks = remDay/7;
    remDay= remDay -(weeks*7);
    printf("%d days is %d year(s), %d week(s) and %d day(s)", days, years, weeks, remDay);
    return 0;
}