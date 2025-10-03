#include <stdio.h>

int main()
{
	int days,weeks=0,years=0,remdays;
	printf("Enter the amount of days you want to convert :");
	scanf("%d", &days);
	while(days>=365)
	{	
		years++;
		days-=365;
	}
	while(days>=7)
	{
		weeks++;
		days-=7;
	}

	printf("Years : %d, Weeks : %d, Remaining days : %d", years,weeks, days);

	return 0;
}