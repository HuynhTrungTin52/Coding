#include <stdio.h>

void multiply_matrices(int *matrix1, int *matrix2, int *result, int rows1, int cols1, int cols2)
{
	for (int i = 0; i < rows1; i++)
	{
		for (int j = 0; j < cols2; j++)
		{
			result[i * cols2 + j] = 0;
			for (int k = 0; k < cols1; k++)
			{
				result[i * cols2 + j] += matrix1[i * cols1 + k] * matrix2[k * cols2 + j];
			}
		}
	}
}

int main()
{
	int rows1, cols1, rows2, cols2;

	printf("Enter the dimensions of matrix 1 (rows cols): ");
	scanf("%d %d", &rows1, &cols1);

	printf("Enter the dimensions of matrix 2 (rows cols): ");
	scanf("%d %d", &rows2, &cols2);

	if (cols1 != rows2)
	{
		printf("Matrix multiplication not possible. Number of columns in matrix 1 must be equal to the number of rows in matrix 2.\n");
		return 1;
	}

	int matrix1[rows1][cols1], matrix2[rows2][cols2], result[rows1][cols2];

	printf("Enter elements of matrix 1:\n");
	for (int i = 0; i < rows1; i++)
	{
		for (int j = 0; j < cols1; j++)
		{
			scanf("%d", &matrix1[i][j]);
		}
	}

	printf("Enter elements of matrix 2:\n");
	for (int i = 0; i < rows2; i++)
	{
		for (int j = 0; j < cols2; j++)
		{
			scanf("%d", &matrix2[i][j]);
		}
	}

	multiply_matrices(&matrix1[0][0], &matrix2[0][0], &result[0][0], rows1, cols1, cols2);

	printf("Resultant matrix:\n");
	for (int i = 0; i < rows1; i++)
	{
		for (int j = 0; j < cols2; j++)
		{
			printf("%d ", result[i][j]);
		}
		printf("\n");
	}

	return 0;
}