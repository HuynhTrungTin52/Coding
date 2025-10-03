#include <stdio.h>

int main()
{
int x,y;
char a='E',b='V',c='E',d='N';
	printf("Enter a number to check if it's odd or even :");
	scanf("%d",&x);
	y=x % 2;
	a=a - y*('E'-'O');
	b=b - y*('V'-'D');	
	c=c - y*('E'-'D');	
	d=d - y*('N'-' ');	
	printf("%d is %c%c%c%c", x, a, b, c, d);
	return 0;
}