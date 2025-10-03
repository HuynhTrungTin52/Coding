#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

// counts number of lines (more robust for general file reading)
// This function is generally not needed if you process line by line
// in a while(fgets(...)) loop and handle newlines explicitly for output formatting.
// Keeping it for consistency with original intent, but consider if it's truly necessary.
int newlinecount(FILE *fin) {
    int count = 0;
    int c;
    while ((c = fgetc(fin)) != EOF) {
        if (c == '\n') {
            count++;
        }
    }
    // If the file is not empty and doesn't end with a newline, count the last line
    if (count > 0 && fseek(fin, -1, SEEK_END) == 0 && fgetc(fin) != '\n') {
        count++;
    } else if (count == 0 && fseek(fin, 0, SEEK_END) == 0 && ftell(fin) > 0) { // non-empty file without newlines
        count = 1;
    }
    rewind(fin); // Reset file pointer for subsequent reading
    return count;
}

// prevent newline and carriage return
void preventnewline(char *str) {
    str[strcspn(str, "\n\r")] = '\0';
}

// change all char to lowercase
void lowercase(char *str) {
    for (int i = 0; str[i] != '\0'; i++) {
        if (isupper(str[i])) {
            str[i] = tolower(str[i]);
        }
    }
}

// check if the parameter is a valid integer (positive or negative)
bool is_valid_integer(const char *str) {
    if (!str || *str == '\0') {
        return false;
    }
    int i = 0;
    if (str[i] == '-' || str[i] == '+') {
        i++;
    }
    if (str[i] == '\0') { // only a sign character, no digits
        return false;
    }
    while (str[i] != '\0') {
        if (!isdigit(str[i])) {
            return false;
        }
        i++;
    }
    return true;
}

// if the result is float, round it to 2 decimal
double round_to_two_decimals(double num) {
    return floor(num * 100 + 0.5) / 100; // Correct rounding for positive and negative numbers
}

int main() {
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    if (fin == NULL || fout == NULL) {
        fprintf(stderr, "error\n");
        return 1;
    }

    char line_buffer[256]; // Increased buffer size for safety, and renamed to avoid confusion
    int total_lines = newlinecount(fin);
    int current_line_num = 0;

    // calculation for operations
    while (fgets(line_buffer, sizeof(line_buffer), fin) != NULL) {
        preventnewline(line_buffer);
        lowercase(line_buffer);

        char temp_line[256]; // Create a temporary copy for strtok to avoid modifying the original line_buffer for subsequent parsing
        strcpy(temp_line, line_buffer);

        char *operator_str = strtok(temp_line, " ");

        bool invalid_operation = false;

        if (operator_str == NULL) {
            invalid_operation = true; // Empty line or just spaces
        } else {
            // Basic operations (2 parameters)
            if (strcmp(operator_str, "+") == 0 || strcmp(operator_str, "-") == 0 ||
                strcmp(operator_str, "*") == 0 || strcmp(operator_str, "/") == 0 ||
                strcmp(operator_str, "**") == 0 || strcmp(operator_str, "%") == 0) {

                char *num1_str = strtok(NULL, " ");
                char *num2_str = strtok(NULL, " ");
                char *extra_token = strtok(NULL, " "); // Check for extra tokens

                if (!is_valid_integer(num1_str) || !is_valid_integer(num2_str) || extra_token != NULL) {
                    invalid_operation = true;
                } else {
                    int num1 = atoi(num1_str);
                    int num2 = atoi(num2_str);

                    if (strcmp(operator_str, "+") == 0) {
                        fprintf(fout, "%d", num1 + num2);
                    } else if (strcmp(operator_str, "-") == 0) {
                        fprintf(fout, "%d", num1 - num2);
                    } else if (strcmp(operator_str, "*") == 0) {
                        fprintf(fout, "%d", num1 * num2);
                    } else if (strcmp(operator_str, "/") == 0) {
                        if (num2 == 0) {
                            fprintf(fout, "error");
                        } else {
                            double result = (double)num1 / num2;
                            fprintf(fout, "%.2f", round_to_two_decimals(result));
                        }
                    } else if (strcmp(operator_str, "**") == 0) {
                        if (num1 == 0 && num2 == 0) {
                            fprintf(fout, "%d", 1);
                        } else {
                            double result = pow(num1, num2);
                            fprintf(fout, "%.2f", round_to_two_decimals(result));
                        }
                    } else if (strcmp(operator_str, "%") == 0) {
                        if (num2 == 0) {
                            fprintf(fout, "error");
                        } else {
                            fprintf(fout, "%d", num1 % num2);
                        }
                    }
                }
            } else if (strcmp(operator_str, "avg") == 0 || strcmp(operator_str, "min") == 0 ||
                       strcmp(operator_str, "max") == 0) {

                int numbers[10];
                int count_params = 0;
                char *token = NULL;

                // Loop to read parameters dynamically (1 to 10)
                for (int i = 0; i < 10; i++) { // Max 10 parameters
                    token = strtok(NULL, " ");
                    if (token == NULL) {
                        break; // No more tokens, valid if at least 1 was read
                    }
                    if (!is_valid_integer(token)) {
                        invalid_operation = true;
                        break;
                    }
                    numbers[i] = atoi(token);
                    if(numbers[i]>100 || numbers[i]<-100) {
                        invalid_operation=true;
                        break;
                    }
                    count_params++;
                }

                // Check for extra tokens if not already invalid
                if (!invalid_operation && strtok(NULL, " ") != NULL) {
                    invalid_operation = true; // Too many parameters
                }
                
                // If no parameters were read for avg, min, max, count, it's an error
                if (count_params == 0) {
                    invalid_operation = true;
                }

                if (!invalid_operation) {
                    if (strcmp(operator_str, "avg") == 0) {
                        long long sum = 0; // Use long long for sum to prevent overflow
                        for (int i = 0; i < count_params; i++) {
                            sum += numbers[i];
                        }
                        double result = (double)sum / count_params;
                        fprintf(fout, "%.2f", round_to_two_decimals(result));
                    } else if (strcmp(operator_str, "min") == 0) {
                        int min_val = numbers[0];
                        for (int i = 1; i < count_params; i++) {
                            if (numbers[i] < min_val) {
                                min_val = numbers[i];
                            }
                        }
                        fprintf(fout, "%d", min_val);
                    } else if (strcmp(operator_str, "max") == 0) {
                        int max_val = numbers[0];
                        for (int i = 1; i < count_params; i++) {
                            if (numbers[i] > max_val) {
                                max_val = numbers[i];
                            }
                        }
                        fprintf(fout, "%d", max_val);
                    }
                }
            } else {
                invalid_operation = true; // Unknown operator
            }
        }

        if (invalid_operation) {
            fprintf(fout, "error");
        }

        current_line_num++;
        if (current_line_num < total_lines) {
            fprintf(fout, "\n");
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}