#include <stdio.h>

int main()
{
    // Exercise 8
    int x,y;
    char a='Y',b='E',c='S';
    printf("Enter two numbers to find the maximum value of :");
    scanf("%d%d", &x, &y); 
    printf("Is %d > %d ?\n", x, y);
    int check= x<y;
    printf("%c%c%c",a - check*('Y'-'N'), b - check*('E'-'O'), c - check*('S'-' '));
    return 0;
   
}