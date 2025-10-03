//Name : Huynh Trung Tin
//ID : 524k0033
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
typedef struct
{
	char id[25];
	char name[100];
	int program;
	int mathComp;
	float gpa;
	char class;
} SinhVien;
int selSearch(SinhVien student[], char keyID[], int size)
{
	int i;
	for (i = 0; i < size; i++)
	{
		if (strcmp(student[i].id, keyID) == 0)
		{

			return i;
		}
	}
	return -1;
}
void printInfo(SinhVien student);
void claGPA(SinhVien *student);
int findLo(SinhVien student[], int size);
int countG(SinhVien student[],int size);
int main()
{
	SinhVien student[] = {"524k0011", "Nguyen Gia Phuc", 3, 0, 0, ' ',	 // 0
						  "524k0006", "Nguyen Gia Khiem", 6, 2, 0, ' ',	 // 1
						  "524k0033", "Huynh Trung Tin", 10, 10, 0, ' ', // 2
						  "524k0031", "Dinh Ngoc Hoa", 5, 3, 0, ' ',	 // 3
						  "524k0032", "Tran Minh Nghia", 8, 10, 0, ' ',	 // 4
						  "524k0012", "Nguyen Don Thinh", 8, 9, 0, ' '}; // 5

	int i;
	int size = sizeof(student) / sizeof(student[0]);
	for (i = 0; i < size; i++)
	{
		claGPA(&student[i]);
	}
	char choice;
	while (choice != 'q')
	{
		printf("Here is a list of commands :");
		printf("\na. Find a student based on their ID");
		printf("\nb. Find the student with the lowest cumulative GPA");
		printf("\nc. Count how many students are classifed as Good or higher");
		printf("\nq. Quit\n");
		scanf("%c", &choice);

		switch (choice)
		{
		case 'a':
		{
			getchar();
			char keyID[100];
			printf("Enter the ID you want to find :");
			fgets(keyID, 100, stdin);
			keyID[strlen(keyID) - 1] = '\0';
			int foundKey = selSearch(student, keyID, size);

			if (foundKey != -1)
			{
				printf("ID found ! Printing info of ID\n");
				printInfo(student[foundKey]);
				printf("\n\n");
			}
			else
				printf("ID doesn't exist\n\n\n");
			break;
		}
		case 'b':
		{
			int lowest = findLo(student, size);
			printf("The student with the lowest GPA is :\n");
			printInfo(student[lowest]);
			printf("\n\n");
			getchar();
			break;
		}
		case 'c':
		{
			int count = countG(student,size);
			printf("The numbers of Good or Outstanding students are :%d\n\n\n",count);
			getchar();
			break;
		}
		}
	}

	return 0;
}

int countG(SinhVien student[],int size)
{
	int i,count=0;
	for(i=0;i<size;i++)
	{
		if(student[i].gpa >=7) count ++;
	}
return count;
}
int findLoRecursive(SinhVien student[], int size, int index) {
    if (index == size - 1) {
        return index;
    }

    int minIndex = findLoRecursive(student, size, index + 1); 

    if (student[index].gpa < student[minIndex].gpa) {
        return index; 
    } else {
        return minIndex; 
    }
}

int findLo(SinhVien student[], int size) {
    return findLoRecursive(student, size, 0); 
}

void printInfo(SinhVien student)
{
	printf("ID :%s\n", student.id);
	printf("Full name :%s\n", student.name);
	printf("Programming score :%d\n", student.program);
	printf("Math Score :%d\n", student.mathComp);
	printf("GPA :%.1f\n", student.gpa);
	printf("Class :%c\n", student.class);
}
void claGPA(SinhVien *student)
{
	student->gpa = (student->mathComp + student->program) / 2.0;
	if (student->gpa >= 9)
	{
		student->class = 'O';
	}
	else if (student->gpa >= 7)
	{
		student->class = 'G';
	}
	else if (student->gpa >= 5)
	{
		student->class = 'A';
	}
	else
		student->class = 'W';
}