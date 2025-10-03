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

int search(int arr[],int n,int k)
{
	int i,dup=0;
	for(i=0;i<n;i++)
	{
		if(arr[i]==k)
		{
			dup++;
		}
	}
	return dup;
}
int main()
{
	int size;
	int *arr = createArr(&size);
	printf("Enter the key value you want to find :");
	int key;
	scanf("%d",&key);
	int foundDups=search(arr,size,key);
	if(foundDups>0)
	{
		printf("%d",foundDups);
	}else printf("error");
	free(arr);
	return 0;
}