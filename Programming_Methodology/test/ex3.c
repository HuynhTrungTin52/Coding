#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void swap(int* num1,int*num2)
{
	int temp=*num1;
	*num1=*num2;
	*num2=temp;
}

void selectionSort(int arr[],int length)
{
	int minimum;
	
	for(int i=0;i<length;i++)
	{
		minimum=i;
		for(int j=i+1;j<length;j++)
		{
			if(arr[j]<arr[minimum])
			{
				minimum=j;
			}
		}
	swap(&arr[minimum],&arr[i]);
	}
}


int main(int argc, char* argv[])
{
	int arrSize=0;
	int *arr=malloc(sizeof(int)*(arrSize+1));
	
	
	for(int i=1;i<argc;i++)
	{
		int shouldBeNum=1;
		for(int j=0;j<strlen(argv[i]);j++)
		{
			if(isalpha(argv[i][j]) || argv[i][j]=='.')
			{
			printf("Skipping Invalid arguement :%s\n",argv[i]);
			shouldBeNum=0;
			break;
			}
		}
	if(shouldBeNum)
	{
		arr[arrSize]=atoi(argv[i]);
		arrSize++;
		
		arr=realloc(arr,sizeof(int)*(arrSize+1));
	}
	}
selectionSort(arr,arrSize);
printf("The asecending order is :");
for(int i=0;i<arrSize;i++)
{
	printf("%d ",arr[i]);
}
free(arr);

}