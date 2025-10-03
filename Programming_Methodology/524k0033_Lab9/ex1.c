#include <stdio.h>

int main()
{
	int n, sum = 0;
	FILE *infile = fopen("input01.txt", "r");
	FILE *outfile = fopen("output01.txt", "w");
	if (infile == NULL || outfile == NULL)
	{
		printf("Unable to open files");
	}
	while (fscanf(infile, "%d", &n) != EOF)
	{

		sum += n;
	}
	fprintf(outfile, "%d", sum);
	fclose(infile);
	fclose(outfile);
}