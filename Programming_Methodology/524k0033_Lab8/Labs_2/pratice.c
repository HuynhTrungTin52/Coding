#include <stdio.h>
#include <string.h>
#include <math.h>

int main ()
{
	// Exercise 1 : Write a C program to print sum of all even numbers between 1 and n by using 3 loop structures
	// Use do While to validate the input incase the input isn't correct, prompt the user to enter it again
	// Correct input : Minimum of 2
/*
	int n,i;
	int sum =0;
	do 
	{
		printf("The program will print the sum of all even numbers between 1 and :");
		scanf("%d",&n);
	} while (n<1);


	for(i=0; i<=n; i++)
	{
		if(i % 2 ==0)
			{
				sum=sum+i;
			}
	}

	printf("The sum of even numbers between 1 and %d is %d\n",n,sum);
*/
	// Exercise 2 : The above but with odd numbers

	/*
	int n,i;
	int sum=0;
	do 
	{
		printf("The program will print the sum of all odd numbers between 1 and :");
		scanf("%d",&n);
	} while (n<1);


	for(i=0; i<=n; i++)
	{
		if(i % 2 !=0)
			{
				sum=sum+i;
			}
	}

	printf("The sum of odd numbers between 1 and %d is %d\n",n,sum);
*/

	// Exercise 3 :Write a C program to print table of any numbers
	/*
	int i;
	float n;
	printf("Enter the number you want a table of :");
	scanf("%f",&n);
	for (i = 1; i <= 10; i++)
	{
		printf("%.1f x %d = %.1f\n",n,i,n*i);
	}
	*/
	// Exercise 4 : Same as 1 and 2, but with natural numbers
	// 												 : Positive integers
/*	
	int n,i;
	int sum =0;
	do 
	{
		printf("The program will print the sum of all natural numbers between 1 and :");
		scanf("%d",&n);
	} while (n<1);


	for(i=0; i<=n; i++)
	{
		
		if (i>0)
		{
			sum=sum+i;
		}
				
	}

	printf("The sum of natural numbers between 1 and %d is %d\n",n,sum);
*/

// Exercise 5 : Write a C program to find the first and last digits of any number

/*
int j;
char numer[20];

do
{

printf("Enter a number to find the first and last digits of :");
scanf("%s",&numer);
j=strlen(numer)-1;

} while (j<1);

printf("Start of your digit is %c and end of your digit is %c",numer[0],numer[j]);

*/

// Exericse 6 : Write a C program to calculate the sum of digits of any numbers

/*
int j;
int digi[20];
char numer[20];
int sum=0;

do
{

printf("Enter a number to find the sum of the digits of :");
scanf("%s",&numer);
j=strlen(numer)-1;

} while (j<1);

for (int i = 0; i <= j; i++)
{	
	for (int o  = 48; o <= 57; o++)
	{
	if (numer[i]==o) 
	{
		digi[i]=o-48;
	}
	}
	sum=sum+digi[i];
}

	printf("The sum of digits in your number is :%d", sum);
*/


	//Exercise 7 : Write a C program to calculate product of digits of any numbers
/*
int j;
int digi[20];
char numer[20];
int prod=1;

do
{

printf("Enter a number to find the product of the digits of :");
scanf("%s",&numer);
j=strlen(numer)-1;

} while (j<1);

for (int i = 0; i <= j; i++)
{	
	for (int o  = 48; o <= 57; o++)
	{
	if (numer[i]==o) 
	{
		digi[i]=o-48;
	}
	}
	prod=prod*digi[i];
}

	printf("The product of digits in your number is :%d", prod);


*/

	// Exercise 8 : Write a C program to count numbers of digits in a number

/*
int j;
int digi[20];
char numer[20];
char count=0;




printf("Enter a number to find the sum of the digits of :");
scanf("%s",&numer);
j=strlen(numer)-1;



for (int i = 0; i <= j; i++)
{	
	for (int o  = 48; o <= 57; o++)
	{
	if (numer[i]==o) 
	{
		count++;
	}
	}
}

	printf("There is %d numers in your number you entered", count);
	*/
	
// Exericse 9 : Write a C program to swap the first and last digit of a number	

/*
int j;
char numer[20];
int sum=0;
char swapper;

do
{

printf("Enter a number to swap the first and last digit :");
scanf("%s",&numer);
j=strlen(numer)-1;

} while (j<1);

swapper=numer[0];
numer[0]=numer[j];
numer[j]=swapper;


	printf("Here is your number with the first and last digits swapped :%s", numer);
	*/
	

// Exercise 10 : Write a number and print it in reverse
/*	
	
	
int j;
char numer[20];
char remun[20];
int sum=0;
for (int i = 0; i <= 20; i++)
{
	remun[i]=' ';
}

do
{

printf("Enter a number to print it in reverse :");
scanf("%s",&numer);
j=strlen(numer)-1;

} while (j<1);
int o=j;

	for (int i = 0; i <= j; i++,o--)
	{			
		
		
			remun[i]=numer[o];
			
		
		
	}
	
	printf("Here is your number but reverse :%s", remun);
	
	*/
	



// Exericse 11 : Write a C program to check if the number is a palindrome or not
															 //palindrome : the same backward and forward(121,878,72527)
/*
	int j;
char numer[20];
char remun[20];
int sum=0;
char palin =1;
//0 : False; 1 : True
for (int i = 0; i <= 20; i++)
{
	remun[i]=' ';
}




printf("Enter a number to see if it's a palindrome:");
scanf("%s",&numer);
j=strlen(numer)-1;


int o=j;

	for (int i = 0; i <= j; i++,o--)
	{			
		
		
			remun[i]=numer[o];
			
			if (remun[i]!=numer[i])
			{
				palin=0;
			}
			
		
		
	}
	
	if(palin==1)
	{
		printf("The numer above is a palindrome !");
	} else printf("The numer above is NOT a palindrome !");
*/

// Exericse 12 : Check if the number is prime or not, ask the user to input it again
/*	
	int n,i, count=0;
	char prime = 1;
	// 1 : true, 0 : False
	do
	{
	printf("Enter a number to see if it's prime or not(postive integers only) :");
	scanf("%d", &n);
	} while (n<1);
	
	for ( i = 1; i <= n; i++)
	{
		if(n % i == 0)
		{	
			count++;
			
		}
	}
	if(count>2)
	{
		prime=0;
	}
	
	if(prime==1)
	{
		printf("The number above is a prime number");
	} else printf("The number above is NOT a prime number");
	
*/

// Exercise 13 : Write a C program to check if a number is an Armstrong number or not	
/*	
	int n,i,o;
	char j;
	int sum=0;
	int number=0;
	char numer[20];
	int digi[20];
	char armst = 1;
	// 1 : true, 0 : False
	do
	{
	printf("Enter a number to see if it's armstrong or not(postive integers only) :");
	scanf("%s", &numer);
	j=strlen(numer);
	
	} while (j<0);
	
	for ( i = 0; i < j; i++)
{	
	for (int o  = 48; o <= 57; o++)
	{
	if (numer[i]==o) 
	{
		digi[i]=o-48;
	}
	}
	
}
	for ( i = 0; i < j; i++)
	{
		
		sum=sum+pow(digi[i],strlen(numer));
		
	}
	for(i=0; i<j; i++){
		number = number * 10 + (numer[i] - '0');
	}
	if (number==sum)
	{
		printf("The number above is armstrong");
	} else printf("The number above is NOT armstrong");
	
*/
	// Exercise 14: Write a C program to see if it's a perfect number or not 
/*
int i,n;
int digi[20];
int sum=0;
// 1 : true, 0 : false
	do
	{
		printf("Enter a number to see if it's a perfect number or not :");
		scanf("%d",&n);
	} while (n<0);
	
	for ( i = 1; i < n; i++)
	{
		if (n % i ==0)
		{
			
			sum+=i;
		}
	
	}
	if (sum==n)
	{
		printf("The number above is a perfect number");
	} else printf("The number above is NOT a perfect number");
	*/
	
	//Exercise 15 : Write a C program to print all Prime numbers between 1 to N by using all three loop structures. Validating the input incase the input isn't correct by prompting the user to enter it again
	/*
	int N, i;
	int counter;
	do{
	printf("Enter an input to make a range of prime number from 1 to N :");
	scanf("%d", &N);
	} while(N<=1);
	printf("The list of Prime numbers from 1 to %d goes as follows :",N);
		for(i =2; i<=N; i++)
	{ counter=0;
		for(int o=2; o<=i; o++)
		{
			
			
		if (i % o ==0) counter++;
		}
		if (counter<2)
		{
			printf("%d ",i);
		}
	
		
	}
	*/
	//Exercise 16 : Write a C program to print all Armstrong numbers between 1 to N by using all three loop structures. Validating the input incase the input isn't correct by prompting the user to enter it again	
	
	int n;
	printf("Enter an input to make a range of armstrong number from 1 to N :");
	scanf("%d", &n);
	
	
	//Exercise 17 : Write a C program to print all Perfect numbers between 1 to N by using all three loop structures. Validating the input incase the input isn't correct by prompting the user to enter it again	
	
	
	
	
	
	
	
	
	return 0;
}


