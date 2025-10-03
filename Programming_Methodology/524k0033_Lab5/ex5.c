#include <stdio.h>
#include <stdlib.h>

int remove_newline(char str[])
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

	return i;
}


void strcatt(char stringtot[], char string1[], char string2[], int size[])
{
	int i,j,k;
	int size1=size[0];
	int size2=size[1];
	for(i=0;i<size[0];i++)
	{
		printf("%c", string1[i]);
		stringtot[i]=string1[i];
	}
	for(j=i,k=0; k<size[1];j++,k++)
	{
		printf("%c", string2[k]);
		stringtot[j]=string2[k];
	}
}
int main()
{
	char string1[100], string2[100], stringtot[200];
	int size[2];
	printf("Enter string 1:");
	fgets(string1,100,stdin);
	printf("Enter string 2:");
	fgets(string2,100,stdin);
	size[0]=remove_newline(string1);
	size[1]=remove_newline(string2);
	strcatt(stringtot, string1, string2, size);
	return 0;
}