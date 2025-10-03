#include <stdio.h>

int main()
{
	int seconds,minutes=0,hours=0;
	printf("Enter the amount of seconds you want to convert :");
	scanf("%d",&seconds);
	while (seconds>=3600)
	{
		hours+=1;
		seconds-=3600;
	}
	while(seconds>=60)
	{
		minutes++;
		seconds-=60;
	}
	printf("%d hour(s), %d minute(s), %d second(s)",hours,minutes,seconds);
	return 0;
}