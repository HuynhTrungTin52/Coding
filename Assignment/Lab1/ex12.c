#include <stdio.h>


int main()
{
    float angels,angels1,angels2;
    float totang = 0;

    printf("Enter 3 angles to see if it's a triangle or not :");
    scanf("%f%f%f", &angels, &angels1, &angels2);

    totang=angels+angels1+angels2;

    if (totang != 180) printf("This is NOT a triangle");
	else printf("This is a triangle");
    return 0;
}