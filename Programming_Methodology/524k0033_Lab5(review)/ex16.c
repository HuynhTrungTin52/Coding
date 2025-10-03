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

void swap(int *a, int *b)
{
	int temp = *a;
	*a = *b;

	*b = temp;
	printf("After swap, a=%d, b=%d, temp =%d\n", *a, *b, temp);
}

void reversarray(int *arr, int size)
{
	int x, i, j;
	int *begin = arr;
	int *last = arr + size - 1;
		for (i = 0, j = 0; i < size/2; i++, j++)
	{
		swap(begin, last);
        begin++;
        last--;
	}
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

	reversarray(arr,size);
	putchar('\n');
	printarray(arr,size);
	free(arr);
	return 0;
}