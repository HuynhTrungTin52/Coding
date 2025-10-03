#include <stdio.h>

int main()
{

	int i, j;
	int choice;
	printf("Would you like to output a rectangle or triangle ? 1 : Rectangle; 2 : Triangle\n");
	scanf("%d", &choice);
	if (choice == 1)
	{
		int wid, len;
		printf("Enter the width and length respectively of the rectangle :");
		scanf("%d %d", &wid, &len);
		printf("Here is a border only rectangle :\n");
		for (i = 1; i <= wid; i++)
		{
			for (j = 1; j <= len; j++)
			{
				if (i == 1 || i == wid || j == 1 || j == len)
				{
					printf("* ");
				}
				else
					printf("  ");
			}
			printf("\n");
		}
		printf("Here is a field only rectangle :\n");
		for (i = 1; i <= wid; i++)
		{
			for (j = 1; j <= len; j++)
			{

				printf("* ");
			}
			printf("\n");
		}
	}
	else
	{
		int typetri, k = 0;
		int hollowed = 0; // 0 = False; 1 = True
		printf("Which types of triangle would you like to output next ?\n");
		printf("1. Half triangle\n");
		printf("2. Balanced triangle\n");
		printf("3. Upside balanced triangle\n");
		scanf("%d", &typetri);
		printf("\n1 for Hollowed, 0 for Filled :");
		scanf("%d", &hollowed);
		printf("\n");
		if (typetri == 1)
		{
			for (i = 1; i <= 5; i++)
			{
				for (j = 1; j <= i; j++)
				{
					if (hollowed == 1)
					{
						if (j == 1 || j == i || i == 1 || i == 5)
						{
							printf("* ");
						}
						else
							printf("  ");
					}
					else
						printf("* ");
				}
				printf("\n");
			}
		}
		if (typetri == 2)
		{
			for (i = 1; i <= 5; ++i, k = 0)
			{
				for (j = 1; j <= 5 - i; ++j)
				{
					printf("  ");
				}
				int mid = 2 * i - 1;
				while (k != mid)
				{
					if (hollowed == 1)
					{
						int x;
						if (k == 0 || i == 1 || i == 5 || k == mid - 1)
						{
							printf("* ");
						}
						else
							printf("  ");
					}
					else
						printf("* ");

					++k;
				}
				printf("\n");
			}
		}
		if (typetri == 3)
		{
			for (i = 5; i >= 1; i--)
			{
				for (j = 0; j < 5 - i; ++j)
				{
					printf("  ");
				}
				for (k = i; k <= 2 * i - 1; k++)
				{
					if (hollowed == 1)
					{
						if (k == i || i == 5)
							printf("* ");
						else
							printf("  ");
					}
					else
						printf("* ");
				}
				for (k = 0; k < i - 1; k++)
				{
					if (hollowed == 1)
					{
						if (k == i - 2 || i == 5)
							printf("* ");
						else
							printf("  ");
					}
					else
						printf("* ");
				}
				printf("\n");
			}
		}
	}
	return 0;
}