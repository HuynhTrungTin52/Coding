#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
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
char* findchars(char string[])
{
	char *chars=calloc(100,sizeof(char));
	int i,j;
	for(i=0,j=0;i<strlen(string);i++)
	{	
		if(isalpha(string[i]))
		{
			chars[j]=string[i];
			j++;
		}

	}
	return chars;
}
int counter_letters(char letters[],char tar)
{
	int i,count=0;
	for(i=0;i<strlen(letters);i++)
	{
		if(tar==letters[i])
		{
			count++;
		}
	}
	return count;
}
int main()
{
	char string[100];
	int i,j;
	char shouldcont=0;
	// 0= False, 1 = true
	printf("Enter a string :");
	fgets(string,100,stdin);
	remove_newline(string);
	char *letters=findchars(string);
	if(!isalpha(letters[0]))
	{
		printf("There is no letters in your string");
	}
		for(i=0;i<strlen(letters);i++,shouldcont=0)
	{
		for(j=0;j<i;j++)
		{
			if(letters[j]==letters[i])
			{
				shouldcont=1;
			}
		}
		if(shouldcont==1)
		{
			continue;
		}
		printf("There is %d of %c in your string\n",counter_letters(letters,letters[i]),letters[i]);
	}

	free(letters);

	return 0;
}