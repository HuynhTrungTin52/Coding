// Name : Huynh Trung Tin
// ID: 524k0033
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
bool isLeap(double year);
bool fullDays(double month);
typedef struct
{
	int day, month, year;
} date;
bool isValid(date *time, char str[])
{

	char *eDay, *eMonth, *eYear;
	double day = strtod(strtok(str, "/"), &eDay);
	double month = strtod(strtok(NULL, "/"), &eMonth);
	double year = strtod(strtok(NULL, "/"), &eYear);
	bool letterInNumbers = (*eDay != 0 || *eMonth != 0 || *eYear != 0);
	bool fractionDate = (remainder(day, 1) != 0 || remainder(month, 1) != 0 || remainder(year, 1) != 0);
	bool invalidDate = (day > 31 || month > 12 || day < 0 || month < 0 || year < 0);
	if (letterInNumbers || fractionDate || invalidDate)
	{
		printf("Error : Invalid format");
		return false;
	}
	if (!isLeap(year))
	{
		if (month == 2 && day == 29)
		{
			printf("Invalid : Febuary only has 29 days during leap years");
			return false;
		}
	}
	if (!fullDays(month))
	{
		if (day > 30)
		{
			printf("Invalid : Too many days");
			return false;
		}
	}
	time->day=day;
	time->month=month;
	time->year=year;
	return true;
}
int main()
{

	date time1, time2;
	printf("Format : dd/mm/yyyy\nEnter the current day :");
	char present[12], future[12];
	fgets(present, 12, stdin);
	present[strlen(present) - 1] = '\0';
	printf("Enter the destined day :");
	fgets(future, 12, stdin);
	future[strlen(future) - 1] = '\0';
	if(!isValid(&time1,present) || !isValid(&time2,future)) return 1;
	if(time2.year < time1.year)
	{
		printf("The destined day can't be in the past");
		return 1;
	}
	int dYear=time2.year-time1.year;
	int dMonth=time2.month-time1.month;
	int dDay=time2.day-time1.day;

	printf("%d %d %d",dYear,dMonth, dDay);
	//3->6
	//31+30+31+30
	// 142 days
	// 23/3 -> 24/6
	//142 + 1 =143
	// 23/3 -> 10/6
	//142-13 ?

	//1/1/2025 - 2/1/2025 
	return 0;
}

bool fullDays(double month)
{
	switch ((int)month)
	{
	case 1:
		return true;

	case 2:
		return false;
	case 3:
		return true;
	case 4:
		return false;
	case 5:
		return true;
	case 6:
		return false;
	case 7:
		return true;
	case 8:
		return true;
	case 9:
		return false;
	case 10:
		return true;
	case 11:
		return false;
	case 12:
		return true;
	default:
		break;
	}
}
bool isLeap(double year)
{

	// leap year if perfectly divisible by 400
	if (remainder(year, 400) == 0)
	{
		return true;
	}
	// not a leap year if divisible by 100
	// but not divisible by 400
	else if (remainder(year, 100) == 0)
	{
		return false;
	}
	// leap year if not divisible by 100
	// but divisible by 4
	else if (remainder(year, 4) == 0)
	{
		return true;
	}
	// all other years are not leap years
	else
	{
		return false;
	}
}