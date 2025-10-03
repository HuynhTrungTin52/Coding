#include <stdio.h>

int main()
{
	FILE *infile = fopen("input.txt", "r");
	FILE *outfile = fopen("output.txt", "w");
	if (infile == NULL || outfile == NULL)
	{
		printf("Unable to open files");
		return 0;
	}
	int num;

	while (fscanf(infile, "%d", &num) != EOF)
	{
		if (num % 2 != 0)
		{
			fprintf(outfile, "%d ", num);
		}
	}
	fputc('\n', outfile);
	rewind(infile);
	while (fscanf(infile, "%d", &num) != EOF)
	{
		if (num % 2 == 0)
		{
			fprintf(outfile, "%d ", num);
		}
	}
	fclose(infile);
	fclose(outfile);

	return 0;
}