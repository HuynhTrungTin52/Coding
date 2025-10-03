#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int linearSearch(int arr[], int size, int value)
{
	int i;
	for (i = 0; i < size; i++)
	{
		if (arr[i] == value)
			return i;
	}
	return -1;
}
void bubbleSort(int arr[], int size)
{
	int i, limit, temp;
	for (limit = size - 2; limit >= 0; limit--)
	{

		for (i = 0; i <= limit; i++)
		{
			if (arr[i] > arr[i + 1])
			{
				temp = arr[i];
				arr[i] = arr[i + 1];
				arr[i + 1] = temp;
			}
		}
	}
}
int binarySearch(int arr[], int low, int high, int mid, int value)
{

	mid = (low + high) / 2;
	if (mid <= 0)
		return -1;
	else if (arr[mid] == value)
		return mid;
	else if (value > arr[mid])
		binarySearch(arr, mid, high, mid, value);
	else if (value < arr[mid])
		binarySearch(arr, low, mid, mid, value);
}
int main()
{
	char fileName[100], choice;
	int num[100], i = 0, temp, value, index;
	printf("Enter a file name :");
	fgets(fileName, 100, stdin);
	fileName[strlen(fileName) - 1] = '\0';
	FILE *infile = fopen(fileName, "r");
	if (infile == NULL)
	{
		printf("Invalid file name, would you like to try again ?(Y/N)\n");
		scanf("%c", &choice);
		getchar();
		if (choice == 'Y')
		{

			while (infile == NULL || (infile = fopen(fileName, "r")) == 0)
			{
				free(infile);
				printf("Enter a file name :");
				fgets(fileName, 100, stdin);
				fileName[strlen(fileName) - 1] = '\0';

				infile = fopen(fileName, "r");
			}
		}
		else if (choice == 'N')
		{
			return 1;
		}
	}
	while (fscanf(infile, "%d", &temp) != EOF)
	{
		num[i] = temp;
		i++;
	}
	printf("Pick a search algorithim :\n");
	printf("A. Linear Search");
	printf("\nB. Binary Search\n");
	scanf("%c", &choice);
	getchar();
	printf("Enter a value to search for :");
	scanf("%d", &value);
	if (choice == 'A')
	{
		index = linearSearch(num, i, value);
	}
	else if (choice == 'B')
	{
		bubbleSort(num, i);
		index = binarySearch(num, 0, i, 0, value);
	}

	if (index != -1)
		printf("Element found at position %d", index);
	else
		printf("Value not found");
	return 0;
}