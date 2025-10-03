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
void mergearray(int *arr1,int size1	,int *arr2, int size2)
{	int i = 0, j = 0, k = 0;
int size=size1+size2;
	int *mergedArr = malloc(size * sizeof(int));
    // Copy remaining elements from arr1
    while (i < size1) {
        mergedArr[k] = arr1[i];
        i++;
        k++;
    }

    // Copy remaining elements from arr2
    while (j < size2) {
        mergedArr[k] = arr2[j];
        j++;
        k++;
    }
    printf("Merged array: ");
    for (i = 0; i < size1 + size2; i++) {
        printf("%d ", mergedArr[i]);
    }
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
	int size1,size2;
	int i;
	printf("Enter the size of the first array you want :");
	scanf("%d", &size1);
	int *arr1 = arraysize(&size1);
	printarray(arr1, size1);
	putchar('\n');
	printf("Enter the size of the second array you want :");
	scanf("%d", &size2);
	int *arr2 = arraysize(&size2);
	printarray(arr2, size2);
	mergearray(arr1,size1,arr2,size2);
	free(arr1); free(arr2);
	return 0;
}