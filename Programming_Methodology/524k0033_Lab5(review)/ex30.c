#include <stdio.h>
#include <stdlib.h>

int determinant2x2(int **matrix) {
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
}


int determinant(int **matrix, int n) {
    int det = 0;
    if (n == 1) {
        return matrix[0][0];
    } else if (n == 2) {
        return determinant2x2(matrix);
    } else {
        int **submatrix = (int **)malloc((n - 1) * sizeof(int *));
        for (int i = 0; i < n - 1; i++) {
            submatrix[i] = (int *)malloc((n - 1) * sizeof(int));
        }

        for (int i = 0; i < n; i++) {
            int sign = (i % 2 == 0) ? 1 : -1;
            for (int j = 0; j < n - 1; j++) {
                for (int k = 0; k < n - 1; k++) {
                    if (k < i) {
                        submatrix[j][k] = matrix[j + 1][k];
                    } else {
                        submatrix[j][k] = matrix[j + 1][k + 1];
                    }
                }
            }
            det += sign * matrix[0][i] * determinant(submatrix, n - 1);
        }

        for (int i = 0; i < n - 1; i++) {
            free(submatrix[i]);
        }
        free(submatrix);

        return det;
    }
}

int main() {
    int n;

    printf("Enter the size of the matrix: ");
    scanf("%d", &n);

    int **matrix = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    int det = determinant(matrix, n);
    printf("Determinant of the matrix: %d\n", det);



    free(matrix);

    return 0;
}