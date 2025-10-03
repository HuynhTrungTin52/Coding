#include <stdio.h>
#include <string.h>
int main()

{
/*
	//Switch : A basic form of conditional structure, where a value is selected and several actions are listed, one of them activating dependng on the value
	int a;
	printf("Do you like cheese ? (1 for yes, 2 for no) :");
	scanf("%d",&a);
	switch (a)
	{
	case 1:
		printf("Well okay");
		break;
	// Break is necessary to stop the case from pinting out other cases
	case 2:
		printf("Alright");
		break;
	}
*/

// While(loop) : Basic type of loop, a set of commmands that will run nonstop unless it no longer satisfies the conditions
// break and continue : Break means to break out of a loop, and continue is to skip the remaining code
/*
int a = 1;
int b;
	printf("Let's count from 1 to... what number do you want ? ");
	scanf("%d",&b);
	printf("Alright ! Here goes !\n");
	while (a <= 100)
	{
		printf(" %d", a);
		a=a+1;
	}
*/	


//For loop : For has three parts, the initialization statement which is used to state a variable to start off; the second is the evaluation of the tested expression; the third part is the increment statement which is used to increase or decrease the variable in the initialization statement
// Often used with Arrays

/*
	printf("Let's count from 1 to 100 ! ");
for(int i=0; i<=100; i++)
{
	printf("\n%d",i);
}
*/

// Do while : Similar to while, except the command will run once before checking the condition
// Useful for checking if someone's input is valid or not

char name[20];
int lenstr;
int redo =0;
	do 
	{ 
		
		printf("Please input your name :");
	    gets(name);
		lenstr=strlen(name);
		for (int i = 0; i < lenstr; i++)
		{
			if ((65 <= name[i] && name[i] <= 90) || (97 <= name[i] && name[i] <= 122))
			{
				redo=0;
			
			}
			else redo =1;
		}
	
		
	} while (redo ==1);
	printf("So your name is %s, right ?", name);
		

return 0;

}