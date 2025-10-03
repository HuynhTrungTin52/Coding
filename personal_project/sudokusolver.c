#include <stdio.h>
// gcc sudokusolver.c -o main && main
void sudokugrid()
{
	int i, j;
	int wid = 9, len = 9;
	for (i = 1; i <= wid; i++)
	{
		
		for (j = 1; j <= len; j++)
		{
			if (i == 3 || i==7)
			{
				printf("___");
			}
			if(j==9 && i!=1 && i!=9)
			{
				printf("\t|\t|\t|");
			}
			
		}
		if(i<9) printf("\n|",i);
	}
}
int main()
{
	
	sudokugrid();
}