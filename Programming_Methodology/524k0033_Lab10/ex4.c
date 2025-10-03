#include <stdio.h>
#include <string.h>
int palinChecker(char str[])
{
	int i,j;
	for(i=0,j=strlen(str)-1;i<=j;i++,j--)
	{
		if(str[i]!=str[j]) return 0;
	}
return 1;
}
int main()
{
	printf("Enter a string :");
	char str[100];
	fgets(str,100,stdin);
	str[strlen(str)-1]='\0';
	int isPalin = palinChecker(str);
	if(isPalin) printf("The string above is a Palindrome"); else printf("The string above is not a Palindrome");
	return 0;
}