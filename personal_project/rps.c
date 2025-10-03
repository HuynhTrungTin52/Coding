//Name : Huynh Trung Tin
// ID : 524k0033
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include<unistd.h>
char *botDecide(int size)
{
	char *choice=malloc(size * sizeof(char));
	time_t seconds;
	seconds = time(NULL);
	srand(seconds);
	int val=rand()%3+1;
	switch(val)
	{
		case 1 :
		{
			strcpy(choice,"Rock");
			break;
		}
		case 2 :
		{
			strcpy(choice,"Paper");
			break;
		}
		case 3 :
		{
			strcpy(choice,"Scissors");
			break;
		}
	}
return choice;
}
int decideWinner(char choice[], char bChoice[])
{
	char a=choice[0],b=bChoice[0];
	if((a=='R' && b=='S') ||(a=='P' && b=='R') || (a=='S' && b=='P'))
	{
		return 1;
	} else if(a==b || a=='Q') return 2; else return 0;
}
int main()
{
	unsigned char pScore=0,bScore=0;
	char choice[10];
	while(strcmp(choice,"Quit"))
	{
	printf("\nPick one of the three options(type out the word) :");
	printf("\n1.Rock");
	printf("\n2.Paper");
	printf("\n3.Scissors");
	printf("\n4.Quit\n");
	scanf("%s",choice);
	char* bChoice=botDecide(10);
	printf("You picked :%s",choice);
	printf("\nBot picked :%s",bChoice);
	if(decideWinner(choice,bChoice)==1)
	{
		pScore++;
	} else if(decideWinner(choice,bChoice)==0) bScore++;
	printf("\nPlayer score : %d\nBot score : %d\n",pScore,bScore);
	
	sleep(3);
	free(bChoice);
	}
	return 0;
}

