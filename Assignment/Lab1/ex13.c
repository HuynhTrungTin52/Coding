#include <stdio.h>

int main()
{

    float markphysics,markchem,markbio,markmath,markcom,mark;
    char grade;
    double tong=0;
    int i;
    int checker;
    printf("Enter your Physics mark :");
    scanf("%f", &markphysics);
    printf("Enter your Chemistry mark :");
    scanf("%f", &markchem);
    printf("Enter your Biology mark :");
    scanf("%f", &markbio);
    printf("Enter your Mathematics mark :");
    scanf("%f", &markmath);
    printf("Enter your Computer mark :");
    scanf("%f", &markcom);

    tong=(markphysics+markchem+markbio+markmath+markcom)/5*10;

    if (tong >= 90)
        grade = 'A';
    else if (tong >= 80)
        grade = 'B';
    else if (tong >= 70)
        grade = 'C';
    else if (tong >= 60)
        grade = 'D';
    else if (tong >= 40)
        grade = 'E';
    else
        grade = 'F';
    printf("So your overall percentage is %.2f%c and overall grade is %c",tong,37, grade);

    return 0;
}