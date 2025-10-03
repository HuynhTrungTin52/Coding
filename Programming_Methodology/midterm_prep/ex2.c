// Name : Huynh Trung Tin
// Student's Code : 524k0033
#include <stdio.h>

int main()
{
	int d,money=18000,i;
	printf("Enter the distance(km) for your taxi :");
	scanf("%d", &d);
	if(d==0)
	{
		printf("The taxi can't less than 1km, please try again");
	}
	for (i = 1; i <= d; i++)
	{
		if (i > 30)
		{
			money+= 4000;
		} else

		if (i > 10)
		{
			money += 6000;
		}
		if (i < 10)
		{
			money+=8000;
		}
	}
	printf("%d", money);
	return 0;
}