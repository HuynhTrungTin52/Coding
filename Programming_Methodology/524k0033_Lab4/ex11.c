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
void printcounterarray(int *counter, int *arr, int size)
{
	int i, j;
	int skipper = 0;
	// 0 : False,1 : True
	for (i = 0; i < size; i++,skipper=0)
	{
		int checker = arr[i];
		for (j = 0; j < i; j++)
		{
			if (checker == arr[j])
			{
				skipper = 1;
			}
		}
		if (skipper == 1)
		{
			continue;
		}
		else
			printf("There is %d %d-elements in the array\n", counter[i], arr[i]);
	}
}
void counter_array(int *arr, int size)
{
	int i, j;
	int *counter = malloc(size * sizeof(int));

	for (i = 0; i < size; i++)
	{
		counter[i] = 0;
		for (j = 0; j < size; j++)
		{
			if (arr[i] == arr[j])
			{
				counter[i]++;
			}
		}
	}

	printcounterarray(counter, arr, size);
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
	counter_array(arr, size);
	free(arr);
	return 0;
}