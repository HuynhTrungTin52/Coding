#include <stdio.h>
#include <string.h>

int main()
{	char name[40];
	char last_name[25];
	printf("Enter your name :");
	// Assuming the name is from America
	fgets(name,40,stdin);
	name[strlen(name)-1]='\0';
	char *ptr = strtok(name," ");
	printf("First name : %s",ptr);
	while(ptr!=NULL)
	{
		strcpy(last_name,ptr);
		ptr=strtok(NULL," ");
		if(ptr==NULL)
		{
			break;
		}	
	}
	
	printf("\nLast name : %s", last_name);
}