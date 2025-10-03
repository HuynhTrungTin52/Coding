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

int findMax(int arr[], int size)
{
	int max =arr[0];
	int i;
	for(i=1;i<size;i++)
	{
		if(max<arr[i]) max = arr[i];
	}
	return max;
}
int main()
{
	int size;
	int *arr = createArr(&size);
	int maxNum=findMax(arr,size);
	printf("The largest number in your array is :%d", maxNum);
	free(arr);
	return 0;
}