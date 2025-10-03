#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int *createArr(int *size)
{
	printf("Enter size :");
	scanf("%d", size);
	int *arr = malloc(*size * sizeof(int));
	int i;
	for (i = 0; i < *size; i++)
	{
		printf("Enter number for array at index %d :", i);
		scanf("%d", arr + i);
	}
	return arr;
}
bool isOdd(int num)
{
	if (num % 2 !=0)
		return false;
	return true;
}
int totalOdd(int arr[], int size)
{
	const int x =10;
	int i, sum = 0;
	for (i = 0; i < size; i++)
	{
		if (isOdd(arr[i]))
		{
			sum += arr[i];
		}
	}
	return sum;
}
int main()
{
	int size;
	int *arr = createArr(&size);
	int sumOdd = totalOdd(arr, size);
	printf("The sum of odd numbers in your array is :%d", sumOdd);
	free(arr);
	return 0;
}