#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define error_cond 101.0
// conddition for error due to can't ending two functions in one command
void remove_newline(char str[])
{
	// remove and replace '\r' and '\n'
	int i = 0;
	while (i <= strlen(str))
	{
		if (str[i] == '\n' || str[i] == '\r')
		{

			str[i] = '\0';
		}
		i++;
	}
}
void uniletters(char str[])
{
	//Turn any capital letters into lowecase characters to fit the criteria of the midterm
	int i;
	for(i=0;i<strlen(str);i++)
	{
		str[i]=tolower(str[i]);
	}
}
int count_newline(char str[], FILE *f)
{ // to count newlines characters throughout the files
	int counter = 0;
	while (fgets(str, 100, f) != NULL)
	{
		if (str[strlen(str) - 1] == '\n' || str[strlen(str) - 1] == '\r')
		{

			counter++;
		}
	}

	return counter;
}
void decprintf(double result, FILE *f)
{ // Print a number with .02 point of decimal if there is decimals, 0 if not
	if (remainder(result, 1.0) != 0)
	{
		fprintf(f, "%.2lf", trunc(result*100)/100);
	}
	else
		fprintf(f, "%.0lf", result);
}
double *str_to_num(char ope[], int *size)
{
	// The process of turning string into numbers
	double *num = calloc(*size, sizeof(double));
	int i = 0;
	char *token = strtok(NULL, " ");
	// Retrieving the next token of the string
	if (token == NULL)
	{
		num[0] = error_cond;
		// Can't end a function outside of it, so had to return an impossible number
		return num;
	}
	char *endpoint;

	while (token != NULL)
	{
		//Detect any dots on numbers and print out error
		char *temp = token;
		while (*temp)
		{
			if (*temp == '.')
			{
				temp++;
				if (!isdigit((unsigned char)*temp))
				{	// Avoiding array subscript
					num[0] = error_cond;
					return num;
				}
			}

			temp++;
		}
		
		num[i] = strtod(token, &endpoint);
		
		// Using strtod to catch any stray letters,symbols
		if (num[i] > 100 || num[i] < -100 || *endpoint != 0 || i >= *size)
		{
			num[0] = error_cond;
			break;
		}
		i++;
		token = strtok(NULL, " ");
	}
	if(*size==2)
	{//This is to make the arithmetic always have 2 numbers or else errors
		if(i!=2)
		{
			num[0]=error_cond;
		}
	} else *size = i;
	// The common max size is 10, which leaves 0 or uninitialized memory that messes up with the memory
	// Used a Pointer to reduce the amount of size to the appropiate parameters
	return num;
}
void ari_time(char ope[], FILE *f)
{

	double *num;
	int symbly = 0, size = 2;
	int *psize = &size;
	char *tari = strtok(ope, " ");
	// token with arithmetic
	if (strcmp(tari, "+") == 0)
	{
		symbly = 1;
	}
	else if (strcmp(tari, "-") == 0)
	{
		symbly = 2;
	}
	else if (strcmp(tari, "*") == 0)
	{
		symbly = 3;
	}
	else if (strcmp(tari, "/") == 0)
	{
		symbly = 4;
	}
	else if (strcmp(tari, "**") == 0)
	{
		symbly = 5;
	}
	else if (strcmp(tari, "%") == 0)
	{
		symbly = 6;
	}

	num = str_to_num(ope, psize);
	if (num[0] == error_cond)
	{
		fprintf(f, "error");
		return;
	}
	
	switch (symbly)
	{
	case 1:
		decprintf(num[0] + num[1], f);
		break;
	case 2:

		decprintf(num[0] - num[1], f);
		break;
	case 3:

		decprintf(num[0] * num[1], f);
		break;
	case 4:
		if (num[1] == 0)
		{
			fprintf(f, "error");
			return;
		}
		// In case the user put anything divided by 0
		decprintf(num[0] / num[1], f);
		break;
	case 5:

		decprintf(pow(num[0], num[1]), f);
		break;
	case 6:

		decprintf(fmod(num[0],num[1]), f);
		break;
	}
	free(num);
}
void avg_time(char ope[], FILE *f)
{
	double *num;
	int i = 0, size = 10;
	int *psize = &size;
	double sum;
	num = str_to_num(ope, psize);
	if (num[0] == error_cond)
	{
		fprintf(f, "error");
		return;
	}
	for (i = 0; i < size; i++)
	{

		sum += num[i];
	}

	if (i == 1 && num[0] == 0)
		decprintf(0, f);
	else
		decprintf(sum / i, f);
	free(num);
}
void max_min(char ope[], FILE *f)
{

	double *num, target;
	// target is the max and min
	int i, size = 10;
	int *psize = &size;

	num = str_to_num(ope, psize);
	if (num[0] == error_cond)
	{
		fprintf(f, "error");
		return;
	}
	char *taxtin = strtok(ope, " ");
	int minmax = strcmp("max", taxtin) == 0 ? 1 : 0;
	// 1 : Find max
	// 0 : Find min
	target = num[0];
	for (i = 1; i < size; i++)
	{
		
		if (minmax == 1)
		{
			target = (target > num[i]) ? target : num[i];
		}
		else
			target = (target < num[i]) ? target : num[i];
	}
	
	decprintf(target, f);
	free(num);
}
void sumoddeven(char ope[], FILE *f)
{
	int i, orr, n, sum = 0;
	char *endpoint;
	// orr = 0 : Odd
	// orr =1 : Even
	char *tum = strtok(ope, " ");
	// We already have the first word, so we can skip to the next one
	tum = strtok(NULL, " ");
	if ((strcmp(tum, "odd")) == 0)
	{
		orr = 0;
	}
	else if ((strcmp(tum, "even")) == 0)
	{
		orr = 1;
	}
	else
	{
		fprintf(f, "error");
		return;
	}
	tum = strtok(NULL, " ");
	// Moving onto the number
	if (tum == NULL)
	{
		fprintf(f, "error");
		return;
	}
	n = strtol(tum, &endpoint, 10);
	if (n > 100 || n < -100 || *endpoint != 0)
	{
		fprintf(f, "error");
		return;
	}
	for (i = 1; i <= n; i++)
	{
		if (orr == 0)
		{
			if (i % 2 != 0)
			{
				sum += i;
			}
		}
		else if (orr == 1)
		{
			if (i % 2 == 0)
			{
				sum += i;
			}
		}
	}
	fprintf(f, "%d", sum);
}
void pcount(char ope[], FILE *f)
{
	double *n;
	int size = 10;
	int *psize = &size, i, j, counter = 0;
	n = str_to_num(ope, psize);
	if (n[0] == error_cond)
	{
		fprintf(f, "error");
		return;
	}
	for (i = 0; i < size; i++)
	{
		if (n[i] == 1.0 || remainder(n[i], 1) != 0 || n[i]==0.0)
		{

			// One and decimal numbers are not prime numbers, so they can be skipped
			continue;
		}
		for (j = 2; j < n[i]; j++)
		{
			if (remainder(n[i], j) == 0)
			{

				counter--;
				break;
			}
		}
		// If a number got here then they satisfy all conditions to be a prime number
		counter++;
	}
	if(counter<0) counter=0;
	fprintf(f, "%d", counter);
}

void dec2bin(char ope[], FILE *f)
{

	double n, result;
	int i = 0, x, y = 0;
	char deci = 0;
	// deci =0 : There is no decimals; =1 : There is decimals
	char *tec = strtok(ope, " "); // tec(token dec2bin)= dec2bin
	char *endpoint;
	if ((tec = strtok(NULL, " ")) == NULL)
	{
		fprintf(f, "error");
		return;
	}
	n = strtod(tec, &endpoint);
	if (n > 100.0 || n <= 0.0 ||*endpoint != 0)
	{
		fprintf(f, "error");
		return;
	}

	if (remainder(n, 1) != 0)
	{
		n = trunc(n * pow(2.0, 8.0));
		deci = 1;
	}
	while (n >= 1.0)
	{
		x = (int)n % 2;
		y = x * (int)pow(10, i++) + y;
		n = trunc(n / 2);
	}
	result = (deci == 1) ? y / pow(10.0, 8.0) : y;
	decprintf(result, f);
}
void map(char ope[], FILE *f)
{
	double *n;
	int size = 10, *psize = &size, i;
	char *tmap = strtok(ope, " ");
	tmap = strtok(NULL, " ");
	// token map
	n = str_to_num(ope, psize);
	if (n[0] == error_cond)
	{
		fprintf(f, "error");
		return;
	}
	for (i = 0; i < size; i++)
	{

		if (strcmp(tmap, "double") == 0)
		{
			n[i] = n[i] * 2;
		}
		else if (strcmp(tmap, "square") == 0)
		{
			n[i] = pow(n[i], 2);
		}
		else if (strcmp(tmap, "absolute") == 0)
		{
			n[i] = abs(n[i]);
		}
		decprintf(n[i], f);
		if (i != size-1)
			fputc(' ', f);
		// To put a space between each numbers, not leaving an additional space
	}
}
int is_valid(char ope[])
{
	// to account for wasteful spaces
	int i = 0;
	int space_counter = 0;
	int word_counter = 0;

	for (i = 0; i < strlen(ope); i++)
	{
		if (ope[i] == ' ')
		{
			space_counter++;
		}
	}

	char *tko = strtok(ope, " ");
	while (tko != NULL)
	{
		word_counter++;
		tko = strtok(NULL, " ");
	}

	if (space_counter >= word_counter)
	{
		return 1;
		//Is not valid
	}
	else
		return 0;
		//Is Valid
}
int main()
{

	char ope[100], tester[100];
	// Each time a function runs using ope and being tokenized, the string is tokenized and therefore unusable
	// Having a second string variable can restore the tokenized string 
	FILE *infile = fopen("input.txt", "r");
	FILE *outfile = fopen("output.txt", "w");

	if (infile == NULL || outfile == NULL)
	{
		// can't open files
		fprintf(outfile, "error");
		return 1;
	}

	int newline_counter = count_newline(ope, infile);
	rewind(infile);
	// to open the file once again
	while (fgets(ope, 100, infile) != NULL)
	{

		remove_newline(ope);
		uniletters(ope);
		
		if (is_valid(strcpy(tester, ope)) == 1)
		{
			
			fprintf(outfile, "error");
			if (newline_counter != 0)
			{
				fputc('\n', outfile);
				newline_counter--;
			}
			continue;
			//Skip to the next line
		}

		char *token = strtok(strcpy(tester, ope), " ");

		if ((strcmp(token, "+") == 0) || (strcmp(token, "-") == 0) || (strcmp(token, "*") == 0) || (strcmp(token, "/") == 0) || (strcmp(token, "**") == 0) || (strcmp(token, "%") == 0))
		{
			ari_time(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else if (strcmp(token, "avg") == 0)
		{

			avg_time(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else if (strcmp(token, "min") == 0 || strcmp(token, "max") == 0)
		{

			max_min(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else if (strcmp(token, "sum") == 0)
		{
			sumoddeven(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else if (strcmp(token, "count") == 0)
		{
			pcount(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else if (strcmp(token, "dec2bin") == 0)
		{
			dec2bin(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else if (strcmp(token, "map") == 0)
		{
			map(strcpy(tester, ope), outfile);
			if (newline_counter != 0)
				fputc('\n', outfile);
		}
		else
		{
			fprintf(outfile, "error");
			if (newline_counter != 0)
				fputc('\n', outfile);
		}

		newline_counter--;
		//Placing a newline counter after each line in the output
	}

	fclose(infile);
	fclose(outfile);
	return 0;
}