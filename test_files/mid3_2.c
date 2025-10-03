#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

void add(int a,int b,FILE* outfile){
    fprintf(outfile,"%d", a +b );
}
void sub(int a,int b,FILE* outfile){
    fprintf(outfile,"%d", a - b );
}
void mul(int a,int b,FILE* outfile){
    fprintf(outfile,"%d", a * b );
}
void divi(int a,int b,FILE* outfile){
    if(b == 0){
        fprintf(outfile,"error");
    }else{
        fprintf(outfile,"%d", a / b );
    }
}
void power(int a,int b,FILE* outfile){
    fprintf(outfile,"%d", (int)pow(a,b) );
}
void remaind(int a,int b,FILE* outfile){
    fprintf(outfile,"%d", a % b );
}
void average(int n,double a1[],FILE* infile, FILE* outfile){
    double sum = 0;
    int i;
    while(fscanf(infile, "%lf",&a1[i]) == 1){
        sum += a1[i];
        i++;
    } 
    if (sum == 0)
    {
        fprintf(outfile,"%.0lf");
        return;
    }
    fprintf(outfile,"%.2lf", sum / i);
    
}
void min(int a[], int n,FILE*  infile, FILE* outfile){
    int i;
    int min;
    if(fscanf(infile, "%d",&a[0]) == 1){
        min = a[0];
    }
      for(i = 1; i < n;i++)
        {
            if(fscanf(infile, "%d",&a[i]) == 1){
                if (a[i] < min)
                min = a[i];
            }
        }
       
    fprintf(outfile, "%d", min);
}
void max (int a[], int n,FILE*  infile, FILE* outfile){
    int i;
    int max;
    if(fscanf(infile, "%d",&a[0]) == 1){
        max = a[0];
    }
      for(i = 1; i < n;i++)
        {
            if(fscanf(infile, "%d",&a[i]) == 1){
                if (a[i] > max)
                max = a[i];
            }
        }
       
    fprintf(outfile, "%d", max);
}
void sumodd(int n,FILE* infile, FILE* outfile){
    int i;
    while (fscanf(infile, "%d", &n) == 1){
    if( n < 0)
    {
        fprintf(outfile, "error");
    }else{
    int sum = 0;
    for (i = 1; i <= n; i++)
    {
            if (i % 2 == 1)
            {
                sum = sum + i;
            }
        }
        fprintf(outfile, "%d", sum);
    }
    }
}    
void sumeven(int n,FILE* infile, FILE* outfile){
    int i;
    while (fscanf(infile, "%d", &n) == 1){
        if( n < 0)
    {
        fprintf(outfile, "error");
    }else{
    int sum = 0;
    for (i = 1; i <= n; i++)
    {
            if (i % 2 == 0)
            {
                sum = sum + i;
            }
        }
        fprintf(outfile, "%d", sum);
    }
    }
} 
int primeNumber(int n){
    int prime = 1;
    int i;
    if(n <= 1) return 0;
    for( i = 2; i <= n / 2;i++){
        if (n % i == 0)
        {
            prime = 0;
            break;
        }
    }
    return prime;
}
void count(FILE* infile, FILE* outfile){
    int n,countnumber = 0;
    while(fscanf(infile, "%d", &n) == 1){
        if (primeNumber(n)){
            countnumber++;
        }
    }
    fprintf(outfile, "%d",countnumber);
}
void convertBin(int n, FILE* outfile){
    if ( n > 1){
        convertBin(n/2, outfile);
    }
    fprintf(outfile, "%d", n % 2);
}
void printBin(FILE* infile, FILE* outfile){
    int n;
    while (fscanf(infile, "%d", &n) == 1){
        if ( n <= 0){
            fprintf(outfile, "error");
        }else{
            convertBin(n,outfile);
            fprintf(outfile, "");
        }
    }
}
void mDouble(int* n,FILE* infile, FILE* outfile){
    while (fscanf(infile, "%d",n ) == 1)
    {
        int result = *n * 2;
         fprintf(outfile, "%d ", result);
    }
    fprintf(outfile,"");
}
void mSquare(int* n,FILE* infile, FILE* outfile){
    while (fscanf(infile, "%d",n ) == 1)
    {
        int result = *n * *n;
         fprintf(outfile, "%d ", result);
    }
    fprintf(outfile,"");
}
void mAbsolute(int* n,FILE* infile, FILE* outfile){
    while (fscanf(infile, "%d",n ) == 1)
    {
        int result = abs(*n);
         fprintf(outfile, "%d ", result);
    }
    fprintf(outfile,"");
}
int whiteSpace(char a){
    return (a == ' ');
}
void checkSpace(char* n, FILE* outfile){
    int i;
    for( i = 0; *n != '\0';i++){
        if(whiteSpace(*n) && whiteSpace(*n + 1)){
            fprintf(outfile, "error");
        }
    }
}

int main(){
    FILE* infile=fopen("input.txt", "r");
    FILE* outfile=fopen("output.txt", "w");
    if(infile == NULL || outfile == NULL)
    {
        printf("unable to open files\n");
        return 1;
    }
    char operation[20];
    int a,b,firsttime=0;
    while(fscanf(infile,"%s",operation) != EOF)
    {
        if(firsttime !=0) fprintf(outfile,"\n");
        int i;
        firsttime++;
        for (i = 0; operation[i]; i++)
        {
            operation[i] = tolower(operation[i]);
        }
        
        if(strcmp(operation,"+") == 0)
        {
            fscanf(infile,"%d %d",&a,&b);
            add(a,b,outfile);
        }
        else if(strcmp(operation,"-") == 0)
        {
            fscanf(infile,"%d %d",&a,&b);
            sub(a,b,outfile);
        }else if(strcmp(operation,"*") == 0)
        {
            fscanf(infile,"%d %d",&a,&b);
            mul(a,b,outfile);
        }else if(strcmp(operation,"/") == 0)
        {
            fscanf(infile,"%d %d",&a,&b);
            divi(a,b,outfile);
        }else if(strcmp(operation,"**") == 0)
        {
            fscanf(infile,"%d %d",&a,&b);
            power(a,b,outfile);
        }else if(strcmp(operation,"%") == 0)
        {
            fscanf(infile,"%d %d",&a,&b);
            remaind(a,b,outfile);
        }else if(strcmp(operation, "avg") == 0)
        {
            int n = 10;
            double a1[100];
            average(n,a1,infile,outfile);
        }else if(strcmp(operation, "min") == 0){
            int n ;
            int a[100];
            min(a,n,infile,outfile);
        }else if(strcmp(operation, "max") == 0){
            int n ;
            int a[100];
            max(a,n,infile,outfile);
        }else if(strcmp(operation, "sum") == 0){
            int n;
            fscanf(infile,"%s",operation);
            
            if(strcmp(operation,"odd")==0)
            {
                sumodd(n,infile,outfile);
            } else if(strcmp(operation, "even") == 0){
            
            sumeven(n,infile,outfile);
            } 
        }else if(strcmp(operation, "count") == 0){
            count(infile,outfile);
        }else if(strcmp(operation, "dec2bin") == 0){
            printBin(infile,outfile);
    }else if (strcmp(operation, "map") == 0){
        int* n;
        int count;
        fscanf(infile,"%s",operation);
        if(strcmp(operation,"double")==0)
            {
                mDouble(n,infile,outfile);
            }
        else if (strcmp(operation, "square") == 0)
        {
            mSquare(n,infile,outfile);
        }else if(strcmp(operation,"absolute")==0)
        {
            mAbsolute(n,infile,outfile);
        } else fprintf(outfile,"error");
        
    }
    }
    



    fclose(infile);
    fclose(outfile);
    return 0;
}
