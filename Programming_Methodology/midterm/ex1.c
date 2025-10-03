#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define ERROR_VALUE 101.0

void sanitizeString(char *inputString) {
    for (int i = 0; inputString[i]; i++) {
        if (inputString[i] == '\n' || inputString[i] == '\r') {
            inputString[i] = '\0';
        }
    }
}

void convertToLowerCase(char *inputString) {
    for (int i = 0; inputString[i]; i++) {
        inputString[i] = tolower((unsigned char)inputString[i]);
    }
}

int countNewlinesInFile(char *buffer, FILE *filePointer) {
    int count = 0;
    while (fgets(buffer, 100, filePointer)) {
        count++;
    }
    return count;
}

void printFormattedDouble(double value, FILE *filePointer) {
    if (fabs(value - (int)value) > 0.001) {
        fprintf(filePointer, "%.2lf", trunc(value * 100) / 100);
    } else {
        fprintf(filePointer, "%.0lf", value);
    }
}
double *parseNumbersFromString(char *operationString, int *numCount) {
    double *numbers = calloc(*numCount, sizeof(double));
    int i = 0;
    char *token = strtok(NULL, " ");
    if (token == NULL) {
        numbers[0] = ERROR_VALUE;
        return numbers;
    }
    char *endPtr;
    while (token != NULL) {
        // Check for valid numeric format: optional +/-, only one dot, no extra characters
        int len = strlen(token);
        int dotCount = 0, signCount = 0, digitCount = 0;
        for (int j = 0; j < len; j++) {
            char ch = token[j];
            if (j == 0 && (ch == '+' || ch == '-')) {
                signCount++;
            } else if (ch == '.') {
                dotCount++;
                if (dotCount > 1 || j == len - 1 || j == 0) {
                    numbers[0] = ERROR_VALUE;
                    return numbers;
                }
            } else if (!isdigit((unsigned char)ch)) {
                numbers[0] = ERROR_VALUE;
                return numbers;
            } else {
                digitCount++;
            }
        }
        if (signCount > 1 || digitCount == 0) {
            numbers[0] = ERROR_VALUE;
            return numbers;
        }
        numbers[i] = strtod(token, &endPtr);
        if (*endPtr != '\0' || numbers[i] > 100 || numbers[i] < -100 || i >= *numCount) {
            numbers[0] = ERROR_VALUE;
            return numbers;
        }
        i++;
        token = strtok(NULL, " ");
    }
    if (*numCount == 2 && i != 2) {
        numbers[0] = ERROR_VALUE;
    } else {
        *numCount = i;
    }
    return numbers;
}

void performArithmeticOperation(char *operationString, FILE *filePointer) {
    double *numbers;
    int operationType = 0;
    int size = 2;
    int *psize = &size;
    char *operation = strtok(operationString, " ");
    if (operation == NULL || strlen(operation) > 2) {
        fprintf(filePointer, "error");
        return;
    }
    if (strcmp(operation, "+") == 0) operationType = 1;
    else if (strcmp(operation, "-") == 0) operationType = 2;
    else if (strcmp(operation, "*") == 0) operationType = 3;
    else if (strcmp(operation, "/") == 0) operationType = 4;
    else if (strcmp(operation, "**") == 0) operationType = 5;
    else if (strcmp(operation, "%") == 0) operationType = 6;
    else {
        fprintf(filePointer, "error");
        return;
    }

    numbers = parseNumbersFromString(NULL, psize);
    if (numbers[0] == ERROR_VALUE) {
        fprintf(filePointer, "error");
        free(numbers);
        return;
    }

    switch (operationType) {
        case 1:
            printFormattedDouble(numbers[0] + numbers[1], filePointer);
            break;
        case 2:
            printFormattedDouble(numbers[0] - numbers[1], filePointer);
            break;
        case 3:
            printFormattedDouble(numbers[0] * numbers[1], filePointer);
            break;
        case 4:
            if (numbers[1] == 0) {
                fprintf(filePointer, "error");
            } else {
                printFormattedDouble(numbers[0] / numbers[1], filePointer);
            }
            break;
        case 5:
            printFormattedDouble(pow(numbers[0], numbers[1]), filePointer);
            break;
        case 6:
            printFormattedDouble(fmod(numbers[0], numbers[1]), filePointer);
            break;
    }
    free(numbers);
}

void calculateAverage(char *operationString, FILE *filePointer) {
    int size = 10;
    double *numbers = parseNumbersFromString(operationString, &size);
    if (numbers[0] == ERROR_VALUE) {
        fprintf(filePointer, "error");
        return;
    }
    double sum = 0;
    for (int i = 0; i < size; i++) sum += numbers[i];
    printFormattedDouble(size == 0 ? 0 : sum / size, filePointer);
    free(numbers);
}

void findMinMax(char *operationString, FILE *filePointer) {
    char *token = strtok(operationString, " ");
    int size = 10;
    double *numbers = parseNumbersFromString(NULL, &size);
    if (numbers[0] == ERROR_VALUE) {
        fprintf(filePointer, "error");
        return;
    }
    double result = numbers[0];
    for (int i = 1; i < size; i++) {
        if (strcmp(token, "max") == 0) {
            if (numbers[i] > result) result = numbers[i];
        } else {
            if (numbers[i] < result) result = numbers[i];
        }
    }
    printFormattedDouble(result, filePointer);
    free(numbers);
}

void calculateSumOfOddOrEven(char *operationString, FILE *filePointer) {
    strtok(operationString, " ");
    char *type = strtok(NULL, " ");
    char *numStr = strtok(NULL, " ");
    if (!type || !numStr) {
        fprintf(filePointer, "error");
        return;
    }
    char *end;
    int limit = strtol(numStr, &end, 10);
    if (*end || limit < 0 || limit > 100) {
        fprintf(filePointer, "error");
        return;
    }
    int even = strcmp(type, "even") == 0;
    int sum = 0;
    for (int i = 1; i <= limit; i++) {
        if ((i % 2 == 0) == even) sum += i;
    }
    fprintf(filePointer, "%d", sum);
}

void countPrimeNumbers(char *operationString, FILE *filePointer) {
    int size = 10;
    double *numbers = parseNumbersFromString(operationString, &size);
    if (numbers[0] == ERROR_VALUE) {
        fprintf(filePointer, "error");
        return;
    }
    int count = 0;
    for (int i = 0; i < size; i++) {
        int n = numbers[i];
        if (n < 2 || numbers[i] != n) continue;
        int isPrime = 1;
        for (int j = 2; j * j <= n; j++) {
            if (n % j == 0) {
                isPrime = 0;
                break;
            }
        }
        count += isPrime;
    }
    fprintf(filePointer, "%d", count);
    free(numbers);
}

void convertDecimalToBinary(char *operationString, FILE *filePointer) {
    strtok(operationString, " ");
    char *token = strtok(NULL, " ");
    if (!token) {
        fprintf(filePointer, "error");
        return;
    }
    char *end;
    double val = strtod(token, &end);
    if (*end || val <= 0 || val > 100) {
        fprintf(filePointer, "error");
        return;
    }
    int isDecimal = remainder(val, 1.0) != 0.0;
    if (isDecimal) val = trunc(val * pow(2, 8));
    long long binary = 0, factor = 1;
    while ((long long)val > 0) {
        binary += ((long long)val % 2) * factor;
        val = trunc(val / 2);
        factor *= 10;
    }
    if (isDecimal) {
        printFormattedDouble((double)binary / pow(10, 8), filePointer);
    } else {
        printFormattedDouble(binary, filePointer);
    }
}

void performMappingOperation(char *operationString, FILE *filePointer) {
    strtok(operationString, " ");
    char *type = strtok(NULL, " ");
    int size = 10;
    double *numbers = parseNumbersFromString(NULL, &size);
    if (numbers[0] == ERROR_VALUE) {
        fprintf(filePointer, "error");
        return;
    }
    for (int i = 0; i < size; i++) {
        if (strcmp(type, "double") == 0) {
            numbers[i] *= 2;
        } else if (strcmp(type, "square") == 0) {
            numbers[i] *= numbers[i];
        } else if (strcmp(type, "absolute") == 0) {
            numbers[i] = fabs(numbers[i]);
        }
        printFormattedDouble(numbers[i], filePointer);
        if (i != size - 1) fputc(' ', filePointer);
    }
    free(numbers);
}

int isInputValid(char *operationString) {
    int wordCount = 0;
    char temp[100];
    strcpy(temp, operationString);
    char *token = strtok(temp, " ");
    while (token != NULL) {
        wordCount++;
        token = strtok(NULL, " ");
    }
    int spaceCount = 0;
    for (int i = 0; operationString[i]; i++) {
        if (operationString[i] == ' ') spaceCount++;
    }
    return spaceCount >= wordCount;
}

int main() {
    char operation[100], copy[100];
    FILE *in = fopen("input.txt", "r");
    FILE *out = fopen("output1.txt", "w");
    if (!in || !out) return 1;

    int lines = countNewlinesInFile(operation, in);
    rewind(in);

    while (fgets(operation, 100, in)) {
        sanitizeString(operation);
        convertToLowerCase(operation);
        strcpy(copy, operation);

        if (isInputValid(copy)) {
            fprintf(out, "error");
            if (--lines) fputc('\n', out);
            continue;
        }

        char *type = strtok(copy, " ");

        if (!strcmp(type, "+") || !strcmp(type, "-") || !strcmp(type, "*") ||
            !strcmp(type, "/") || !strcmp(type, "**") || !strcmp(type, "%")) {
            performArithmeticOperation(operation, out);
        } else if (!strcmp(type, "avg")) {
            calculateAverage(operation, out);
        } else if (!strcmp(type, "min") || !strcmp(type, "max")) {
            findMinMax(operation, out);
        } else if (!strcmp(type, "sum")) {
            calculateSumOfOddOrEven(operation, out);
        } else if (!strcmp(type, "count")) {
            countPrimeNumbers(operation, out);
        } else if (!strcmp(type, "dec2bin")) {
            convertDecimalToBinary(operation, out);
        } else if (!strcmp(type, "map")) {
            performMappingOperation(operation, out);
        } else {
            fprintf(out, "error");
        }

        if (--lines) fputc('\n', out);
    }

    fclose(in);
    fclose(out);
    return 0;
}
