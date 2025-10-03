#include <stdio.h>

int main()
{
    int n;
    int i = 1;
    printf("Here are the multiplication tables of 1 to 10 :\n");
    while (i <= 10)
    {
        int o = 1;
        while (o <= 10)
        {
            printf("%dx%d=%d\t", o, i, i * o);
            if (o == 10)
                printf("\n");
            o++;
        }

        i++;
    }
    return 0;
}