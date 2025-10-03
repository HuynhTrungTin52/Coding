#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

int ch_range_num(char *str, double *val) 
{
    char *e; 
    val = strtok(str, e);
    if((str == e) && (*e != '\0') && (*val > -100 || *val < 100)) return 0;

    return 1;
}
double *str_to_num(char);
int cp_simple(char * str, double *val)
{

}

int main()
{
    FILE *fi;
    FILE *fo;
    
    fi = fopen("input.txt","r");
    fo = fopen("output.txt","w");

    if(fi == NULL || fo == NULL) // nếu ko mở file
    {
        fprintf(fo ,"error");
        return 1;
    }
    int n;
    fscanf(fi, "%d", &n);
    printf("%d",n);
    int i;
    for(i = 0; i < n; i++)
    {
        
    }
    

    fclose(fi);
    fclose(fo);
    
    return 0;

}