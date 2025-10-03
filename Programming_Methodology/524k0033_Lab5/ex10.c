#include <stdio.h>
#include <string.h>

int main()
{
	char string1[100],string2[100];
	int posi;
	printf("Enter your string 1:");
	fgets(string1,100,stdin);
	string1[strlen(string1)-1]='\0';
	printf("Enter your string 2:");
	fgets(string2,100,stdin);
	string2[strlen(string2)-1]='\0';
	printf("Enter the position where str2 replaces str1 :");
	scanf("%d", &posi);
	strncpy(&string1[posi],string2,strlen(string2));
	printf("String 1 with string 2 mashed in from %d index :%s",posi, string1);


	return 0;
}