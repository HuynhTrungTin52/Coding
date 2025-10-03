#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int newlines_solver(char str[])
{
	int i = 0, counter = 0;
	while (i <= strlen(str))
	{
		if (str[i] == '\n' || str[i] == '\r')
		{
			counter++;
			str[i] = '\0';
		}
		i++;
	}
	return counter;
}
int main()
{
	FILE *infile = fopen("input02.txt", "r");
	FILE *outfile = fopen("output02.txt", "w");
	char str[100];
	int i = 0, newcounter = 0;
	// if (infile == NULL || outfile == NULL)
	// {
	// 	printf("Unable to open files");
	// }
	while (fgets(str, 100, infile) != NULL)
	{

	// char *token = strtok(str," ");
	// token=strtok(NULL," ");
	// int num1=atoi(token);
	// token=strtok(NULL," ");
	// int num2=atoi(token);
	// fprintf(outfile,"%d",num1+num2);    		
	// 	newcounter = newlines_solver(str);
	// 	i++;
	// 	fprintf(outfile, "The length of the %d string is : %d", i, strlen(str));

	// 	if (newcounter != 0)
	// 		fputc('\n', outfile);
	// 	newcounter--;
	printf("%s",str);
	}
	fclose(infile);
	fclose(outfile);
}