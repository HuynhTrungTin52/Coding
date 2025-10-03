#include <stdio.h>
#include <math.h>

double determinant(int *matrix, int n) {
    if (n == 1) {
        return matrix[0];
    } else {
        double det = 0;
        for (int i = 0; i < n; i++) {
            int submatrix[n - 1][n - 1];
            int subrow = 0, subcol = 0;
            for (int j = 0; j < n; j++) {
                if (j != i) {
                    submatrix[subrow][subcol++] = matrix[j * n + i];
                    if (subcol == n - 1) {
                        subcol = 0;
                        subrow++;
                    }
                }
            }
            det += pow(-1, i) * matrix[i] * determinant(&submatrix[0][0], n - 1);
        }
        return det;
    }
}

int main() {
    int n;

    printf("Enter the size of the square matrix: ");
    scanf("%d", &n);

    int matrix[n][n];

    printf("Enter elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    double det = determinant(&matrix[0][0], n);

    printf("Determinant of the matrix: %.2f\n", det);

    return 0;
}