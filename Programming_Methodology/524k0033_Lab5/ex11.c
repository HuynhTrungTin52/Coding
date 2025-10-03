#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
	char *string=calloc(100, sizeof(char));
	int posi,n,i;
	printf("Enter your string :");
	fgets(string,100,stdin);
	string[strlen(string)-1]='\0';
	printf("Enter N and the positon you want to delete :");
	scanf("%d%d", &n, &posi);
	if(posi>=strlen(string))
	{
		printf("Can't delete position that is farther than length of string, the string remains the same :\n%s", string);
	}
	else
	{for(i=posi;i<strlen(string);i++)
	{
		string[i]=string[i+n];
	}
	printf("%s", string);
	}
	return 0;
}