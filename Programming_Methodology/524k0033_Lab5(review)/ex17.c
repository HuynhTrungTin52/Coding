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

void erase_element(int* arr,int size, int deleso)
{
	int i;
	for ( i = deleso; i < size-1; i++)
	{
		arr[i]= arr[i+1];

	}

	
}

void printarray(int *arr, int size)
{ int i;
	for(i=0; i<size;i++)
	{
		printf("a[%d]=%d\n",i,*(arr+i));
	}
}
void printnewarray(int *arr, int size)
{ int i;
	for(i=0; i<size-1;i++)
	{
		printf("a[%d]=%d\n",i,*(arr+i));
	}
}
int main()
{
	int size,i,deleso;
	printf("Enter the size of the array you want :");
	scanf("%d", &size);
	int *arr = arraysize(&size);
	printarray(arr,size);
	printf("Pick a position to erase the element :");
	scanf("%d", &deleso);
	erase_element(arr,size,deleso);
	printnewarray(arr,size);
	return 0;
}