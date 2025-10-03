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
int find_sum(int *arr, int size){
    int sum = 0;
    for(int i = 0; i < size ;i++){
        sum =sum + arr[i];
    }
    return sum;
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
	printf("The sum of elements in the array is :%d", find_sum(arr,size));
	return 0;
}