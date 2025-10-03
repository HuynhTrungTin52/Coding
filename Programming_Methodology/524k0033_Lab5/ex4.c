#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main()
{	char string[200];
	int i;
	printf("Enter a string :");
	fgets(string,200,stdin);
	string[strlen(string)-1]='\0';
	char *token=strtok(string, " ");
	while(token!=NULL)
	{	
		for(i=0;i<strlen(token);i++)
		{
			
			if(i==0)
			{
				token[i]=toupper(token[i]);
				continue;
			}
			if(isupper(token[i]))
			{
				token[i]=tolower(token[i]);
			}
		}
		toupper(token[0]);
		printf("%s ",token);
		token=strtok(NULL," ");
	}

	return 0;
}