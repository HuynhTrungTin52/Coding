#include <stdio.h>

void printa(int a[],int size)
{
	int i;
	for(i=0;i<size;i++)
	{
		printf("%d ",a[i]);
	}
}
void sSort(int a[],int size);
int main()
{
	int a[]={2,5,3,6,1,11,12,34,36,6,31,32,8,4,3,7,10};
	int size=sizeof(a)/sizeof(0);
	printf("Original array :");
	printa(a,size);
	sSort(a,size);
	putchar('\n');
	printf("Sorted array :");
	printa(a,size);



	return 0;	
}

void sSort(int a[], int size)
{
	int i,j,temp;
	for(i=0;i<size-1;i++)
	{
		int min_dex=i;
		for(j=i+1;j<size;j++)
		{
			if(a[j]<a[min_dex]) min_dex=j;
		}		
		temp=a[i];
		a[i]=a[min_dex];
		a[min_dex]=temp;
	}
}	