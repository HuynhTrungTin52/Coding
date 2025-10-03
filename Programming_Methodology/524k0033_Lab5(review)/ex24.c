#include <stdio.h>
#include <stdlib.h>
int *arraysize(int *size)
{
	int i;
	int *a = malloc(*size * sizeof(int));
	for (i = 0; i < *size; i++)
	{
		printf("Enter a[%d] :", i);
		scanf("%d", a + i);
	}
	return a;
}
int *sortarray(int *arr, int size)
{
	int i, j, o = 0;
	int *b = malloc(size * sizeof(int));
	int temp;
	for (i = 0; i < size - 1; i++)
	{
		for (j = 0; j < size - i - 1; j++)
		{
			if ((arr[j]) > (arr[j + 1]))
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
	return arr;
}
void printarray(int *arr, int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		printf("a[%d]=%d\n", i, *(arr + i));
	}
}
int main()
{
	int size;
	int i;
	printf("Enter the size of the array you want :");
	scanf("%d", &size);
	int *arr = arraysize(&size);
	printarray(arr, size);
	putchar('\n');
	int *sortedarray = sortarray(arr, size);
	printarray(sortedarray, size);
	return 0;
}