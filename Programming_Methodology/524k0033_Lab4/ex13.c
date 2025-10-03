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

void splitarray(int *even, int *odd,int arr[], int size)
{

	int i=0,o=0;
	while(i<size)
	{
		if(arr[i] % 2 ==0)
		{
			even[o]=arr[i];

		}
		if(arr[i] %2 !=0)
		{
			odd[o]=arr[i];
		}
	i++,o++;	
	}

}
int countodd(int *arr, int size)
{
	int i, counterodd=0;
	
}
void printarray(int *arr, int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		printf("a[%d]=%d\n", i, *(arr + i));
	}
}
int main()
{
	int size;
	int i;
	int *even = malloc(size * sizeof(int));
	int *odd = malloc(size * sizeof(int));
	printf("Enter the size of the array you want :");
	scanf("%d", &size);
	int *arr = arraysize(&size);
	printarray(arr, size);
	putchar('\n');
	splitarray(even,odd,arr,size);
	printarray(even,size);
	free(arr);
	return 0;
}