#include <stdio.h>

int bSearch(int a[],int size, int key)
{
	int start=0,end=size-1,mid;
	while(start<=end)
	{
		mid=(start+end)/2;
		if(key==a[mid])
		{
			return mid;
		} else if(key>a[mid])
				{
					start=mid+1;
				} else end=mid-1;
						

	}
	return -1;
}
int main()
{
	int a[]={1,2,3,4,5,6,7,8,10,11,12,31,32,34,36};
	int size=sizeof(a)/sizeof(0);
	int key;
	printf("Enter the key you want :");
	scanf("%d", &key);
		if(bSearch(a,size,key)==-1)
	{
		printf("There's no key in the array");
	} else printf("%d",bSearch(a,size,key));
}