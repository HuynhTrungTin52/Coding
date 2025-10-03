#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
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
bool fullDays(double month)
{
	switch ((int)month)
	{
	case 1:
		return true;
		
	case 2: return false;
	case 3: return true;
	case 4: return false;
	case 5: return true;
	case 6: return false;
	case 7: return true;
	case 8: return true;
	case 9: return false;
	case 10: return true;
	case 11: return false;
	case 12: return true;
	default:
		break;
	}
}
int main()
{
	printf("Format : dd/mm/yyyy\nEnter the day, month, and year :");
	// dd/mm/yyyy
	char date[12];
	fgets(date, 12, stdin);
	date[strlen(date) - 1] = '\0';
	char *eDay, *eMonth, *eYear;
	double day = strtod(strtok(date, "/"), &eDay);
	double month = strtod(strtok(NULL, "/"), &eMonth);
	double year = strtod(strtok(NULL, "/"), &eYear);
	bool letterInNumbers = (*eDay != 0 || *eMonth != 0 || *eYear != 0);
	bool fractionDate = (remainder(day, 1) != 0 || remainder(month, 1) != 0 || remainder(year, 1) != 0);
	bool invalidDate=(day>31 || month > 12 || day <0 || month <0);
	if (letterInNumbers == true || fractionDate == true || invalidDate == true)
	{
		printf("Error : Invalid format");
		return 1;
	}
	if (!isLeap(year))
	{
		if (month == 2 && day == 29)
		{
			printf("Invalid : Febuary only has 29 days during leap years");
			return 1;
		}
	}
	if(!fullDays(month))
	{
		if(day>30) {printf("Invalid : Too many days");
		return 1;}
	}
	printf("Valid !");
	return 0;
}