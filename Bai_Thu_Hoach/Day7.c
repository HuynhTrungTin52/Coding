//Name : Huynh Trung Tin
//Student's ID : 524k0033

#include <stdio.h>
#include <string.h>
#define size 2

struct employeeDatabase {
	char id[20];
	char name[20];
	char sex;
	int birthYear,phoneNumber, salary;

};
void betgets(char str[])
{
	fgets(str,100,stdin);
	str[strlen(str)-1]='\0';
}
struct employeeDatabase getInfo();
void printInfo(struct employeeDatabase);
int main()
{
	int i;
	
	struct employeeDatabase emp[size];
	for(i=0;i<size;i++)
	{
		printf("Enter the datas for your no.%d employee :\n",i);
		emp[i]=getInfo();
		putchar('\n');
	}

	while(1)
	{
		printf("If you want to exit, press CTRL+C");
		printf("\nFinding an employee by their id");
		char keyID[100];
				int i;
				printf("\n\nEnter an ID to search :");
				betgets(keyID);
				for(i=0;i<size;i++)
				{
					if(strcmp(keyID,emp[i].id)==0)
					{
						printf("ID found !\n");
						printInfo(emp[i]);
						printf("\nPress enter to continue\n");
						getchar();
						break;
					}
					if(i==size-1) printf("ID not found\n");
				}
			}
		
	
	return 0;

}
struct employeeDatabase getInfo()
{
	struct employeeDatabase emp;
	printf("Enter the ID of employee :");
	betgets(emp.id);
	printf("Enter the name of employee :");
	betgets(emp.name);
	printf("Enter the sex of employee(M for male, F for female, O for others) :");
	scanf(" %c",&emp.sex);
	printf("Enter the birth year of employee :");
	scanf(" %d",&emp.birthYear);
	printf("Enter the phone number of employee :");
	scanf(" %d",&emp.phoneNumber);
	printf("Enter the salary of your employee :");
	scanf(" %d",&emp.salary);
	getchar();
	return emp;
}

void printInfo(struct employeeDatabase emp)
{
	printf("ID : %s\n",emp.id);
	printf("Name :%s",emp.name);
	printf("Sex : %c\n",emp.sex);
	printf("Birth year : %d\n",emp.birthYear);
	printf("Phone number : %d\n",emp.phoneNumber);
	printf("Salary : %d\n",emp.salary);
}