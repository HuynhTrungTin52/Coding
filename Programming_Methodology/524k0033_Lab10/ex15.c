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
void bSort(int a[], int size)
{
	int i, limit, temp;
	for (limit = size - 1; limit > 0; limit--)
	{
		for (i = 0; i < limit; i++)
		{
			if (a[i] > a[i + 1])
			{
				temp = a[i];
				a[i] = a[i + 1];
				a[i + 1] = temp;
			}
		}
	}
}
int search(int arr[],int n,int k)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(arr[i]==k)
		{
			return i;
		}
	}
	return -1;
}
int main()
{
	int size;
	int *arr = createArr(&size);
	printf("Sorting the array...\n");
	bSort(arr,size);
	printf("Enter the key value you want to find :");
	int key;
	scanf("%d",&key);
	int foundValue=search(arr,size,key);
	if(foundValue!=-1)
	{
		printf("%d",foundValue);
	}else printf("error");
	free(arr);
	return 0;
}