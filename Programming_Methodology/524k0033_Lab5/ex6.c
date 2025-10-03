#include <stdio.h>
#include <string.h>
#include <stdlib.h>
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
int findchar(char string[])
{	int i;
	for(i=0;i<strlen(string);i++)
	{
		if(isalpha(string[i]))
		{
		return i;
		} 
	}
	if(1==1)
	{
		return -1;
	}
}
int main()
{
	char *string=malloc(100*sizeof(char));
	printf("Enter a string :");
	fgets(string,100,stdin);
	remove_newline(string);
	if(findchar(string)==-1)
	printf("There is no characters in your string");
	else
	printf("Character '%c' appears at index %d", string[findchar(string)],findchar(string));
	free(string);
}