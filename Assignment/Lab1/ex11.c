#include <stdio.h>

int main()
 {
 char charac;
    int i,j;
    int lowletter = 0;
	int capletter = 0;
    int number = 0;
	//0 : False, 1 : True

    printf("Type in your character: ");
    scanf("%s",&charac);

    capletter = ( 65 <= charac && charac <= 90 );
	lowletter = ( 97 <= charac && charac <= 122 );
	number = (48 <= charac && charac <= 57);

    if ((capletter == 1) || (number == 1) || (lowletter == 1)) 
	{
        printf("This character is alphanumeric !");
    }   
	else 
	{
        printf("This character is NOT alphanumeric !"); 
	}
	return 0;
}