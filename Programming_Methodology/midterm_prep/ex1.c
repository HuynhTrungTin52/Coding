//Name : Huynh Trung Tin
//Student's code : 524k0033

#include <stdio.h>

int main()
{
	int i, h;
	float m, sumh = 0;
	// h: working hours, m : money paid by the hours
	printf("Enter the hours you have worked :");
	scanf("%d", &h);
	for (i = 1; i <= h; i++)
	{
		if (i > 50)
		{
			sumh += 2.6;
		} else
		if (i > 45)
		{
			sumh += 2.5;
		} else
		if (i > 40)
		{
			sumh += 1.8;
		} 
		if (i <= 40)
		{
			sumh++;
		}
	}
	m = sumh * 80;
	printf("%.2f", m);
	return 0;
}