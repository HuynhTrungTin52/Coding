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
bool isPrime(int num)
{
	if (num <= 1)
		return false;
	int i;
	for (i = 2; i < num; i++)
	{
		if (num % i == 0)
		{
			return false;
		}
	}
	return true;
}
int totalPrime(int arr[], int size)
{
	int i, sum = 0;
	for (i = 0; i < size; i++)
	{
		if (isPrime(arr[i]))
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
	int sumPrime = totalPrime(arr, size);
	printf("The sum of prime numbers in your array is :%d", sumPrime);
	free(arr);
	return 0;
}