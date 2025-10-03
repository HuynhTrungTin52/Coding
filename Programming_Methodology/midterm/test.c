#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

// count the number of lines
int newlinecount(FILE *fin)
{
	int count = 0;
	int c;
	while ((c = fgetc(fin)) != EOF)
	{
		if (c == '\n')
		{
			count++;
		}
	}

	// count the last line (if file doesnt end with newline and isnt empty)
	if (count > 0 && fseek(fin, -1, SEEK_END) == 0 && fgetc(fin) != '\n')
	{
		count++;
	}
	else if (count == 0 && fseek(fin, 0, SEEK_END) == 0 && ftell(fin) > 0)
	{ // if file isnt empty
		count = 1;
	}
	rewind(fin);
	return count;
}

// prevent newline and carriage return
void preventnewline(char *str)
{
	str[strcspn(str, "\n\r")] = '\0';
}

// change all char to lowercase
void lowercase(char *str)
{
	int i;
	for (i = 0; str[i] != '\0'; i++)
	{
		if (isupper(str[i]))
		{
			str[i] = tolower(str[i]);
		}
	}
}

// check if the parameter is valid (positive or negative)
bool validation(const char *str)
{
	if (!str || *str == '\0')
	{
		return false;
	}
	int i = 0;
	if (str[i] == '-' || str[i] == '+')
	{
		i++;
	}
	if (str[i] == '\0')
	{ // only a sign character, no digits
		return false;
	}
	bool decimalpoint = false;
	while (str[i] != '\0')
	{
		if (str[i] == '.')
		{
			if (decimalpoint)
			{ // more than one decimal point
				return false;
			}
			decimalpoint = true;
		}
		else if (!isdigit(str[i]))
		{
			return false;
		}
		i++;
	}
	return true;
}

// check if parameter is valid (for 1 parameter)
bool validation2(const char *str)
{
	if (!str || *str == '\0')
	{
		return false;
	}
	int i = 0;
	if (str[i] == '+')
	{
		i++;
	}
	if (str[i] == '\0')
	{ // only a sign character, no digits
		return false;
	}
	bool decimalpoint = false;
	while (str[i] != '\0')
	{
		if (str[i] == '.')
		{
			if (decimalpoint)
			{ // more than one decimal point
				return false;
			}
			decimalpoint = true;
		}
		else if (!isdigit(str[i]))
		{
			return false;
		}
		i++;
	}
	return true;
}

// count the number of spaces in the string
int countspaces(char *str)
{
	int i = 0;
	int countspace = 0;
	while (str[i] != '\0')
	{
		if (str[i] == ' ')
		{
			countspace++;
		}
		i++;
	}
	return countspace;
}

// if the result is float, round it to 2 decimal
double decimal(double num)
{
	return floor(num * 100 + 0.5) / 100;
}

// do prime counting
bool isprime(int num)
{
	if (num < 2)
	{
		return false;
	}
	int i;
	for (i = 2; i <= sqrt(num); i++)
	{
		if (num % i == 0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");

	if (fin == NULL || fout == NULL)
	{
		fprintf(stderr, "error\n");
		return 1;
	}

	char linebuffer[256]; // increased buffer size
	int totallines = newlinecount(fin);
	int currentline = 0;

	// calculation for operations
	while (fgets(linebuffer, sizeof(linebuffer), fin) != NULL)
	{
		preventnewline(linebuffer);
		lowercase(linebuffer);
		bool invalid = false; // register true whenever a false-condition is met

		char temp[256]; // create a temporary copy for strtok (avoid possible bugs)
		strcpy(temp, linebuffer);

		char *operator = strtok(temp, " ");

		if (operator == NULL)
		{ // check if operator is NULL or if there are more than 2 spaces
			invalid = true;
		}
		else
		{
			// basic operations (2 parameters)
			if (strcmp(operator, "+") == 0 || strcmp(operator, "-") == 0 || strcmp(operator, "*") == 0 || strcmp(operator, "/") == 0 || strcmp(operator, "**") == 0 || strcmp(operator, "%") == 0)
			{

				char *num1_str = strtok(NULL, " ");
				char *num2_str = strtok(NULL, " ");
				char *extra = strtok(NULL, " "); // check for extra tokens

				if (!validation(num1_str) || !validation(num2_str) || extra != NULL || countspaces(linebuffer) > 2)
				{ // check if number is valid
					invalid = true;
				}
				else
				{
					int num1 = atoi(num1_str);
					int num2 = atoi(num2_str);

					if (strcmp(operator, "+") == 0)
					{
						fprintf(fout, "%.2f", decimal(num1 + num2));
					}
					else if (strcmp(operator, "-") == 0)
					{
						fprintf(fout, "%.2f", decimal(num1 - num2));
					}
					else if (strcmp(operator, "*") == 0)
					{
						fprintf(fout, "%.2f", decimal(num1 * num2));
					}
					else if (strcmp(operator, "/") == 0)
					{
						if (num2 == 0)
						{
							fprintf(fout, "error");
						}
						else
						{
							double result = (double)num1 / num2;
							fprintf(fout, "%.2f", decimal(result));
						}
					}
					else if (strcmp(operator, "**") == 0)
					{
						if (num1 == 0 && num2 == 0)
						{
							fprintf(fout, "%d", 1);
						}
						else
						{
							double result = pow(num1, num2);
							fprintf(fout, "%.2f", decimal(result));
						}
					}
					else if (strcmp(operator, "%") == 0)
					{
						if (num2 == 0)
						{
							fprintf(fout, "error");
						}
						else
						{
							fprintf(fout, "%d", num1 % num2);
						}
					}
				}
			}
			else if (strcmp(operator, "avg") == 0 || strcmp(operator, "min") == 0 || strcmp(operator, "max") == 0 || strcmp(operator, "count") == 0 || strcmp(operator, "map") == 0)
			{
				int map_to = 0;
				// 1 : double
				// 2 :square
				// 3 : absolute
				int numbers[10];
				int countparams = 0;
				char *token = NULL;
				int i = 0;

				// loop to read parameters (1 to 10 or less)
				for (i = 0; i < 10; i++)
				{
					token = strtok(NULL, " ");
					if (token == NULL)
					{
						break;
					}
					if (strcmp(token, "double") == 0 || strcmp(token, "square") == 0 || strcmp(token, "absolute") == 0)
					{
						countparams++;
						if (strcmp(token, "double") == 0)
							map_to = 1;
						else if (strcmp(token, "square") == 0)
							map_to = 2;
						else if (strcmp(token, "absolute") == 0)
							map_to = 3;
						i--;
						continue;
					}
					if (!validation(token))
					{

						invalid = true;
						break;
					}

					numbers[i] = atoi(token);

					if (numbers[i] > 100 || numbers[i] < -100)
					{ // validation range
						invalid = true;
						break;
					}
					countparams++;
				}
				// check for extra tokens
				if (!invalid && strtok(NULL, " ") != NULL)
				{
					invalid = true; // mark true if exceeded 10 parameters
				}

				// counting the parameters (1 to 10 or less)
				if (countparams == 0)
				{

					invalid = true;
				}

				// check for extra spaces (10 parameters)
				int countspace = countspaces(linebuffer);
				if (countspace > countparams)
				{

					invalid = true;
				}
				if (!invalid)
				{
					if (strcmp(operator, "avg") == 0)
					{
						double avgresult = 0;
						int sum = 0;
						for (i = 0; i < countparams; i++)
						{
							sum += numbers[i];
						}
						avgresult = sum / countparams;
						fprintf(fout, "%.2f", decimal(avgresult));
					}
					else if (strcmp(operator, "min") == 0)
					{
						float minresult = numbers[0];
						for (i = 1; i < countparams; i++)
						{
							if (minresult > numbers[i])
							{
								minresult = numbers[i];
							}
						}
						fprintf(fout, "%.2f", decimal(minresult));
					}
					else if (strcmp(operator, "max") == 0)
					{
						float maxresult = numbers[0];
						for (i = 1; i < countparams; i++)
						{
							if (maxresult < numbers[i])
							{
								maxresult = numbers[i];
							}
						}
						fprintf(fout, "%.2f", decimal(maxresult));
					}
					else if (strcmp(operator, "count") == 0)
					{
						int primecount = 0;
						for (i = 0; i < countparams; i++)
						{
							if (isprime(numbers[i]))
							{
								primecount++;
							}
						}
						fprintf(fout, "%d", primecount);
					}
					// check for map operations
					else if (strcmp(operator, "map") == 0)
					{

						if (map_to == 0)
						{
							invalid = true;
						}
						else if (map_to == 1)
						{

							float doubleresult = 0;
							for (i = 0; i < countparams - 1; i++)
							{
								numbers[i] *= 2;
								doubleresult = numbers[i];
								fprintf(fout, "%.2f", decimal(doubleresult));
								if (i < countparams - 2)
									fputc(' ', fout);
							}
						}
						else if (map_to == 2)
						{
							float squareresult = 0;
							for (i = 0; i < countparams - 1; i++)
							{
								numbers[i] *= numbers[i];
								squareresult = numbers[i];
								fprintf(fout, "%.2f", decimal(squareresult));
								if (i < countparams - 2)
									fputc(' ', fout);
							}
						}
						else if (map_to == 3)
						{
							float absresult = 0;
							for (i = 0; i < countparams - 1; i++)
							{
								if (numbers[i] < 0)
								{
									numbers[i] = abs(numbers[i]);
									absresult = numbers[i];
									fprintf(fout, "%.2f", decimal(absresult));
									if (i < countparams - 2)
										fputc(' ', fout);
								}
							}
						}
						else
						{
							invalid = true;
						}
					}
				}
			}
			else
			{
				invalid = true;
			}

			if (invalid == true)
			{
				fprintf(fout, "error");
			}

			currentline++;
			if (currentline < totallines)
			{
				fprintf(fout, "\n");
			}
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}