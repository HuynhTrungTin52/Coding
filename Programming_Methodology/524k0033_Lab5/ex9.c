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

char *coic(char string1[], char string2[])
{
	int i,j,y,k=0;
	char *a=calloc(100, sizeof(char));
	a[0]='\0';
	for(i=0;i<strlen(string1);i++)
	{
		for(j=0;j<strlen(string1);j++)
		{
		if(string2[i]==string1[j])
		{	
			
			a[k]=string2[i];
			k++;
			break;
		}
		}

	}
	if(strcmp(a,string2)!=0)
	{
		a[0]='\0';
	}
	return a;
}
int main()
{
	char string1[100],string2[100];
	printf("Enter your string 1:");
	fgets(string1,100,stdin);
	printf("Enter your string 2:");
	fgets(string2,100,stdin);
	remove_newline(string1);
	remove_newline(string2);
	char *strr=coic(string1,string2);
	if(strr[0]=='\0')
	{
		printf("String 2 doesn't exist in string 1");
	}else
	printf("The string 2 exist in your string 1 as : %s", strr);
	free(strr);
	return 0;
}