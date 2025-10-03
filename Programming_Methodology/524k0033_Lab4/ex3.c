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
int find_min(int *arr, int n )
{
 int   min=arr[0];
    for (int i = 1; i < n; i++){
       if (min>=arr[i])
       {min=arr[i];}
    }
    return min;
}

void printarray(int *arr, int size)
{ int i;
	for(i=0; i<size;i++)
	{
		printf("a[%d]=%d\n",i,*(arr+i));
	}
}
int main()
{
	int size;
	int i;
	printf("Enter the size of the array you want :");
	scanf("%d", &size);
	int *arr = arraysize(&size);
	printarray(arr,size);
	printf("The min element in the array is :%d", find_min(arr,size));
	return 0;
}