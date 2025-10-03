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
bool isEven(int num)
{
	if (num % 2 !=0)
		return false;
	return true;
}
int totalEven(int arr[], int size)
{
	const int x =10;
	int i, sum = 0;
	for (i = 0; i < size; i++)
	{
		if (isEven(arr[i]))
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
	int sumEven = totalEven(arr, size);
	printf("The sum of even numbers in your array is :%d", sumEven);
	free(arr);
	return 0;
}