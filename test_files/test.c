#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

//counts number of lines
int newlinecount(FILE *fin){
    int count=0;
    char str[100];
    while(fgets(str,100,fin)!=NULL){
        if(str[strlen(str)-1]=='\n'||str[strlen(str)-1]=='\r'){
            count++;
        }
    }
    return count;
}

//prevent newline
void preventnewline(char *str){
    int i=0;
    while(1){
        if(str[i]=='\n'||str[i]=='\r'){
            str[i]='\0';
            break;
        }
        i++;
    }
}

//change all char to lowercase
void lowercase(char *str){
    int i=0;
    while(str[i]!='\0'){
        if(isupper(str[i])){
            str[i]=tolower(str[i]);
        }
        i++;
    }
}

//check if the parameter is a valid negative number(because if check it normally, the - will be mistaken as a char, therefore invalid)
bool validation(const char *str){
    if(!str||*str=='\0'){
        return false;
    }
    int i=0;
    if(str[i]=='-'||str[i]=='+'){
        i++;
    }
    while(str[i]!='\0'){
        if(!isdigit(str[i])){
            return false;
        }
        i++;
    }
    return true;
}

//check for extra spaces (for basic operations aka 2 parameters operations)
int countspaces(char*str){
    int i=0;
    int countspace=0;
    while(str[i]!='\0'){
        if(str[i]==' '){
            countspace++;
        }
        i++;
    }
    return countspace;
}

//if the result is float, round it to 2 decimal
double decimal(double num){
    return floor(num*100)/100;
}

int main(){
    FILE *fin=fopen("input.txt","r");
    FILE *fout=fopen("output.txt","w");

    if(fin==NULL||fout==NULL){
        fprintf(stderr,"error\n");
        return 1;
    }

    //string in input.txt
    char str[100];
    int lines=newlinecount(fin);
    int atline=0;
    rewind(fin);
    
    //calculation for basic operations
    while(fgets(str,100,fin)!=NULL){
        preventnewline(str);
        lowercase(str);

        //count the spaces between each tokens
        int countspace=countspaces(str);

        //extract first tokens
        char *operator=strtok(str," ");

        //check valid for basic operations
        if(operator!=NULL){
            //calculation for 2 parameters
            if(strcmp(operator,"+")==0||strcmp(operator,"-")==0||strcmp(operator,"*")==0||strcmp(operator,"/")==0||strcmp(operator,"**")==0||strcmp(operator,"%")==0){
                
                char *num1_str=strtok(NULL," ");
                char *num2_str=strtok(NULL," ");
                
                int i=0;
                //reset string to count the space(for basic operations)
                bool invalid=false;
                i=0;

                //check if number is valid
                if(validation(num1_str)==false||validation(num2_str)==false||countspace>2){
                    invalid=true;
                }

                if(invalid==false){
                    
                    //convert string to int
                    int num1=atoi(num1_str);
                    int num2=atoi(num2_str);

                    //basic calculations
                    if(strcmp(operator,"+")==0){
                        fprintf(fout,"%d",num1+num2);
                    }else if(strcmp(operator,"-")==0){
                        fprintf(fout,"%d",num1-num2);
                    }else if(strcmp(operator,"*")==0){
                        fprintf(fout,"%d",num1*num2);
                    }else if(strcmp(operator,"/")==0){
                        if(num2==0){
                            fprintf(fout,"error");
                        }else{
                            double result=(double)num1/num2;
                            fprintf(fout,"%.2f",decimal(result));
                        }
                    }else if(strcmp(operator,"**")==0){
                        if(num1==0&&num2==0){
                            fprintf(fout,"%d",1);
                        }else{
                            double result=pow(num1,num2);
                            fprintf(fout,"%.2f",decimal(result));
                        }
                    }else if(strcmp(operator,"%")==0){
                        if(num2==0){
                            fprintf(fout,"error");
                        }else{
                            fprintf(fout,"%d",num1%num2);
                        }
                    }
                }else if(invalid==true){
                    fprintf(fout,"error");
                }
            } //calculation for 10 parameters
            else if(strcmp(operator,"avg")==0||strcmp(operator,"min")==0||strcmp(operator,"max")==0||strcmp(operator,"count")==0){

                //lots of tokens
                char *num1_str=strtok(NULL," ");
                char *num2_str=strtok(NULL," ");
                char *num3_str=strtok(NULL," ");
                char *num4_str=strtok(NULL," ");
                char *num5_str=strtok(NULL," ");
                char *num6_str=strtok(NULL," ");
                char *num7_str=strtok(NULL," ");
                char *num8_str=strtok(NULL," ");
                char *num9_str=strtok(NULL," ");
                char *num10_str=strtok(NULL," ");

                //check if string has more than 2 spaces (for 10 parameters calculation)
                int i=0;

                //reset string to count the space(for 10 parameters calculation)
                bool invalid=false;
                i=0;

                //check if number is valid
                if(validation(num1_str)==false||validation(num2_str)==false||validation(num3_str)==false||validation(num4_str)==false||validation(num5_str)==false||validation(num6_str)==false||validation(num7_str)==false||validation(num8_str)==false||validation(num9_str)==false||validation(num10_str)==false||countspace>10){
                    invalid=true;
                }
                    
                if(invalid==false){

                    //convert string to int
                    int num1=atoi(num1_str);
                    int num2=atoi(num2_str);
                    int num3=atoi(num3_str);
                    int num4=atoi(num4_str);
                    int num5=atoi(num5_str);
                    int num6=atoi(num6_str);
                    int num7=atoi(num7_str);
                    int num8=atoi(num8_str);
                    int num9=atoi(num9_str);
                    int num10=atoi(num10_str);

                    //calculation for 10 parameters
                    if(strcmp(operator,"avg")==0){
                        double result=(double)(num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)/10;
                        fprintf(fout,"%.2f",decimal(result));
                    }
                }
                   
        }else{
            fprintf(fout,"error");
        }
        }
        if(atline<lines){
            fprintf(fout,"\n");
        }
        atline++;
    }
    
    fclose(fin);
    fclose(fout);
    return 0;
}