#include <stdio.h>
#include <string.h>
#include <ctype.h>
void remove_newline(char str[])
{
	
	int i=0;
		while(1==1)
	{
		if(str[i] =='\n')
		{
			str[i] = '\0';
			break;
		}
		i++;
	}
	
}
int isstring(char string[])
{	int i;
	for(i=0;i<strlen(string);i++)
	{
		if(!isalpha(string[i]))
		{
		return 0;//false
		} 
	} 
	return 1;//true
}
int main()
{
	char string[100];
	printf("Enter a string :");
	fgets(string,100,stdin);
	remove_newline(string);
	char *token=strtok(string," ");
	while(token!=NULL)
	{
		if(isstring(token)==1)
		{
			printf("The first word in your string is :%s", token);
			return 0;
		} else 
		token=strtok(NULL," ");
	}
	printf("There is no words in your string");



	return 0;
}