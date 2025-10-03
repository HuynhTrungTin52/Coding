
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
void printarray(int *arr, int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		printf("a[%d]=%d\n", i, *(arr + i));
	}
}
void search_element(int *arr,int size, int toSearch)
{
int found = 0; 
    int i,j=0;
	int foundarr[size];
    for(i=0; i<size; i++)
    {
 
        if(arr[i] == toSearch)
        {
            foundarr[j]=i;
			j++;
        }
    }


    if(j >= 1)
    {
        printf("\n%d is found at index :\n", toSearch);
		for(i =0; i<j; i++)
		{
			printf("%d\n",foundarr[i]);
		}
    }
    else
    {
        printf("\n%d is not found in the array", toSearch);
    }
}
int main()
{
	int size;
	int i,toSearch;
	printf("Enter the size of the array you want :");
	scanf("%d", &size);
	int *arr = arraysize(&size);
	printarray(arr,size);
    printf("\nEnter element to search: ");
    scanf("%d", &toSearch);
	search_element(arr,size,toSearch);

	

    return 0;
}