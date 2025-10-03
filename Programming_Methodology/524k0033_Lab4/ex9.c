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

int counter_array(int *arr, int size)
{
	int i, j;
	int counter =0;

	for (i = 0; i < size; i++)
	{
	int checker;
		for (j = 0; j < i; j++)
		{
			if(checker==arr[i])
			{ break;} else 
			if (arr[i] == arr[j])
			{
				counter++;
				checker=arr[i];
				break;
			} 
		}
	}
return counter;
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
	printf("The total number of duplicates in Array is %d", counter_array(arr,size));
	free(arr);
	return 0;
}