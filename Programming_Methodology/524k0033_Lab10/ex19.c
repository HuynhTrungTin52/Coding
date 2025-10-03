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

int findMin(int arr[], int size)
{
	int min =arr[0];
	int i;
	for(i=1;i<size;i++)
	{
		if(min<arr[i]) min = arr[i];
	}
	return min;
}
int main()
{
	int size;
	int *arr = createArr(&size);
	int minNum=findMin(arr,size);
	printf("The smallest number in your array is :%d", minNum);
	free(arr);
	return 0;
}