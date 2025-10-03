#include <stdio.h>
#include <string.h>
int main()
{
	char name[25];
	int i=0;
	printf("Enter your name :");
	fgets(name,25,stdin);
	while(1==1)
	{
		if(name[i] =='\n')
		{
			name[i] = '\0';
			break;
		}
		i++;
	}

	printf("Your name has %d letter(s), including spaces if there are", i);

	return 0;
}