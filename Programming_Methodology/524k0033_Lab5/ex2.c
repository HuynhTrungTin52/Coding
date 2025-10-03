#include <stdio.h>
#include <string.h>

int main()
{	int i,j;
	char name[25];
	printf("Enter your name :");
	fgets(name,25,stdin);
	name[strlen(name)-1]='\0';
	for ( i = 0,j=strlen(name)-1; i < strlen(name)/2; i++,j--)
	{
		char temp;
		temp=name[i];
		name[i]=name[j];
		name[j]=temp;
		
	}
	
	printf("Your name in reverse is : %s", name);
}