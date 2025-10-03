#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int isPrime(int n)
{
  for(int i=2;i<=sqrt((int)n);i++)
  {
    if(n%i==0) 
	{
		return -1;}
  }
return 1;
}
 
int main(int argc, char *argv[])
{
  int size = argc-1;
  if(size >1)
  {
    printf("Too many arguments, ending program");
    return 1;
  } else if(size =0)
  {
    printf("No arguement, ending program");
  }
  char* endpoint;
  
  int num=strtol(argv[1],&endpoint,10);
  if(endpoint==argv[1] || *endpoint !='\0')
  {
   
    printf("Only pure numbers, ending program");
    return 1;
  }
    else if(num<0)
    {
      printf("Postive numbers only");
      return 1;
    }
   else 
   { int total=1;
     printf("The main divisors for (%d) are :\n",num);
     for(int i=1;i<=num;i++)
     {
       if(num%i==0)
       {
         printf("%d ",i);
       }
     }
     printf("\n%d=",num);
    int checker=2;
    int savedNum=num;
	if(isPrime(num)==1) 
	{printf("%d",num);}
	else
	{
    while(checker<savedNum)
     {
		
       if(num%checker==0 && isPrime(checker)==1) 
       {
         printf("%d",checker);
         num/=checker;
		 if(num!=1) printf("*");
		 
       } else {
         checker++;
       }
	   
	}
     
	}
}
     }
