#include <stdio.h>

void printa(int a[], int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		printf("%d ", a[i]);
	}
}
void bSort(int a[], int size);
int main()
{
	int a[] = {2, 5, 3, 6, 1, 11, 12, 34, 36, 6, 31, 32, 8, 4, 3, 7, 10};
	int size = sizeof(a) / sizeof(0);
	printf("Original array : ");
	printa(a, size);

	bSort(a, size);
	putchar('\n');
	printf("Sorted array : ");
	printa(a, size);

	return 0;
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