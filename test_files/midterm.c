#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
int main()
{

    FILE *inputFile = fopen("input.txt", "r");
    FILE *outputFile = fopen("output.txt", "w");
    char str[100];
    if (inputFile == NULL || outputFile == NULL)
    {
        printf("Error");
        return 1;
    }

    while (fgets(str, 100, inputFile) != NULL)
    {

        int cond;
        if (str[0] == '+')
        {
            cond = 1;
        }
        else if (str[0] == '-')
        {
            cond = 2;
        }
        else if (str[0] == '*' && str[1] == '*')
        {
            cond = 5;
        }
        else if (str[0] == '*')
        {
            cond = 3;
        }
        else if (str[0] == '/')
        {
            cond = 4;
        }
        else if (str[0] == '%')
        {
            cond = 6;
        } else cond=7;
        if(cond!=7)
        {
        char *token = strtok(str, " ");
        token = strtok(NULL, " ");
        int num1 = atoi(token);
        token = strtok(NULL, " ");
        int num2 = atoi(token);

        
        

        switch (cond)
        {
        case 1:
            fprintf(outputFile, "%d\n", num1 + num2);
            break;
        case 2:
            fprintf(outputFile, "%d\n", num1 - num2);
            break;
        case 3:
            fprintf(outputFile, "%d\n", num1 * num2);
            break;
        case 4:
            fprintf(outputFile, "%d\n", num1 / num2);
            break;
        case 5:
            fprintf(outputFile, "%.0lf\n", pow(num1, num2));
            break;
        case 6:
            fprintf(outputFile, "%d\n", num1 % num2);
            break;
        default:
            break;
        
        }
        } else if(str[0]=='s' && str[1]=='u' && str[2]=='m')
        {
            char *token=strtok(str," ");
            token=strtok(NULL," ");
            if(strcmp(token,"odd")==0)
            {
                int sum=0;
                token=strtok(NULL," ");
                int num=atoi(token);
                int i;
                for(i=0;i<=num;i++)
                {
                    if(i%2!=0)
                    {
                        sum=sum+i;
                    }
                }
            fprintf(outputFile,"%d\n",sum);
            } else if(strcmp(token,"even")==0)
            {
                
                int sum=0;
                token=strtok(NULL," ");
                int num=atoi(token);
                int i;
                for(i=0;i<=num;i++)
                {
                    if(i%2==0)
                    {
                        sum=sum+i;
                    }
                }
            fprintf(outputFile,"%d\n",sum);
            }
        } else if(str[0]=='a' && str[1]=='v'&& str[2]=='g')
        {
            int num[10],i=0,sum=0;
            char *token=strtok(str, " ");
            token=strtok(NULL," ");
            while(token!=NULL)
            {
                
                num[i]=atoi(token);
                sum+=num[i];
                i++;
                token=strtok(NULL," ");

            }
            
            fprintf(outputFile,"%.02lf", 1.0*sum/i);
        } else if(str[0]=='c' && str[1]=='o' && str[2]=='u' && str[3]=='n' && str[4]=='t')
        {
            int num[10],i=0,count=0;
            char *token=strtok(str, " ");
            token=strtok(NULL," ");
            while(token!=NULL)
            {
                
                num[i]=atoi(token);
                int j;
                for(j=2;j<num[i];j++)
                {
                    if(num[i]%j==0)
                    {
                        printf("%d / %d\n",num[i],j);
                        break;
                    } else if(j==num[i]-1) count++;
                }
                i++;
                token=strtok(NULL," ");

            }
            
            fprintf(outputFile,"%d", count);
        }
    }

    fclose(inputFile);
    fclose(outputFile);
    return 0;
}
