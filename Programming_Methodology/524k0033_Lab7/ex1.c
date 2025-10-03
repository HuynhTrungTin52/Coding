#include <stdio.h>


int sSearch(int a[],int size,int key);
int main()
{
	//Sequential Search Algorithim
	int a[]={5,3,1,6,8,7,4,9,10,2};
	int size=sizeof(a)/sizeof(0);
	int key;
	printf("Enter the key you want :");
	scanf("%d", &key);
	if(sSearch(a,size,key)==-1)
	{
		printf("There's no key in the array");
	} else printf("%d",sSearch(a,size,key));



	return 0;
}

int sSearch(int a[],int size, int key)
{
	int i;
	for(i=0;i<size;i++)
	{
		if(a[i]==key)
		{
			return i;
		}
	}
	return -1;
}