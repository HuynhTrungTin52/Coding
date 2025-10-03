#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>
#include <float.h>

int main()
{
	//Exercise 1 : Print out your ame, date of birth and mobile number
	// char* name = "Huynh Trung Tin";
	// char birthdate[] = "04/10/2006";
	// char mobinum[] = "0372564612";

	// printf("My name is %s, I was born in %s and my phone number is %s", name, birthdate, mobinum);
	
	//Exercise 2 : Input 2 numbers and output their +,-,x,/

	// int a,b;
	// printf("Enter their two numbers :");
	// scanf("%d%d", &a, &b);
	// printf("%d + %d = %d\n", a, b, a+b);
	// printf("%d - %d = %d\n", a, b, a-b);
	// printf("%d x %d = %.1f\n", a, b, a*b*1.0);
	// printf("%d / %d = %.1f\n", a, b, 1.0*a/b);
	
	//Exercise 3 : Calculate the perimeter of and area of a rectangle 
	
	//Perimeter = 2(a+b); Area = a*b

	// float height,weight,peri,area;
	
	// printf("Give me the height and width of a rectangle :");
	// scanf("%f%f", &height, &weight);
	// peri = 2.0*(height + weight);
	// area = height*weight;
	// printf("Perimeter and Area of the rectangle are :%.1f, %.1f", peri, area);
	// return 0;


	//Exercise 4 : Convert days into years, weeks and days
 /* int years = 0;
    int weeks = 0;
    float rDays = 0;
    float days;

    printf("Input day number: ");

    scanf ("%f",&days);

    if ( days >= 365 ) {
		
        years =(days / 365);
		
        rDays = days - (years * 365);
	
        if ( rDays >= 7 ) { 
			
            weeks = rDays / 7;
			
            rDays = rDays - (7 * weeks);
			
        }

    }

    printf("The given days result in %d year(s), %d week(s) and %d day(s).", years, weeks, (int)rDays);
*/

// Exercise 5 : Convert Celsius to Farenheit 

/*float cel, faren;
	printf("Enter a Celcius degree :");
	scanf("%f", &cel);
	faren= cel*(1.0*9/5)+32;
	printf("%.2f C is %.2f F",cel,faren);
*/
// Exercise 6 :Write a program to return an absolute value of a number
/*
float truenum;
printf("Enter the number you want the absolute value of :");
scanf("%f", &truenum);
if (truenum<0)
{
	truenum=truenum*-1;
}
	printf("The true value of your number is : %.1f",truenum);

*/
// Exercise 7 : check whether a year is a leap year or not
/*
int year;
	printf("Enter the year you want to check if it's leap or not :");
	scanf("%d",&year);
	if (year % 4 ==0)
		{
		printf("Yep, it's a leap year");
		}
	else printf("Nah, it's not a leap year");
*/
// Exercise 8 : Find the max value of two numbers
/*
float a,b;
printf("Enter the first value :");
scanf("%f",&a);
printf("Enter the second value :");
scanf("%f",&b);
printf("The largest number is : %.2f",fmax(a,b));
*/

//Exercise 9 : Write a program to find the maximum of three numbers

/* float num[3];
float maxnum;
int i;
for (i = 0; i <3; i++)
{
	printf("Enter number %d :",i+1);
	scanf("%f",&num[i]);
}
maxnum=num[0];
for (i = 0; i < 3; i++)
{
	if (num[i]>maxnum)
	{
		maxnum=num[i];
	}
	
}
	printf("So the largest number is : %0.2f", maxnum);
*/

//Exericse 10 : Check if a number is odd or even
/*
	int a;
	printf("Enter a number to check if it's odd or even :");
	scanf("%d",&a);
	if (a % 2==0)
	{
		printf("It's even");
	}
	else 
	{
	printf("It's odd");

	}
*/

//Exercise 11 : Input a charcter to see if it's alphanumeric or not
										//alphanumeric : to have both letters and numbers


/*
     char line[255];
    int i,j;
    bool lowletter = false;
	bool capletter = false;
    bool number = false;

    printf("Type in your character: ");

    scanf("%s",&line);

    j = strlen(line);

    for (i = 0;i < j; ++i) {

        if (( 65 <= line[i] && line[i] <= 90 ) ) {

            capletter = true;

        }
		if (( 97 <= line[i] && line[i] <= 122 ))   
		{
			lowletter =  true;

		}
		if (48 <= line[i] && line[i] <= 57) {

            number = true;

        }

    }

    if ((capletter == true) || (number == true) || (lowletter == true)) {

        printf("1");

    }   else {

        printf("0");
}

*/


//Exercise 12 : Input angles of a triangle and check if the triangle is valid or not
/*
long double angels[2];
long double totang = 0;
for (int i = 0; i <= 2; i++)
{
	printf("Enter angels %d :",i+1);
	scanf("%Lf",&angels[i]);
	totang=totang+angels[i];
}

if (totang != 180.0)
{
	printf("This ain't a triangle chief");
} else 
{
	printf("You done it chief, tis a triangle");
}
*/

//Exericse 13 : Grade 5 subjects depending on the marks :Physics, Chemistry, Biology, Mathematics and Computer

const char *subjects[5];
subjects[0] = "Physics";
subjects[1] = "Chemistry";
subjects[2] = "Biology";
subjects[3] = "Mathematics";
subjects[4] = "Computer";

float marksub[5];
char grade;
double tong;
int i;
int checker;
bool redo = false;
	for ( i = 0; i <=4 ; i++)
	{
		printf("Enter your %s's marks :", subjects[i]);
		checker=scanf("%f", &marksub[i]);
		if( (checker != 1) || (marksub[i]>10) )
		{
			redo = true;
			
		} 
		while (redo == true)
			{
				printf("you have entered an invalid character for your marks, try again :");
				if((scanf("%f", &marksub[i])==1) || (marksub[i]<=10))
				{
					redo=false;
				}

			}
			
		tong+=marksub[i];

	}

	
     tong=tong/5*10;

if (tong >= 90) {
        grade = 'A';
    } else if (tong >= 80) 
	{
        grade = 'B';
    } 
	else if (tong >= 70) 
	{
        grade = 'C';
    } 
	else if (tong >= 60) 
	{
        grade = 'D';
    } 
	else if (tong >= 40) 
	{
        grade = 'E';
    } else 
	{
        grade = 'F';
    }
printf("So your overall percentage is %.2f%c and overall grade is %c",tong,37, grade);




}
