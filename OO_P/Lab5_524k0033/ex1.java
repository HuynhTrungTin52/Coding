package Lab5_524k0033;

public class ex1 {

    public static int[][] addMatrices(int[][] matrix1, int[][] matrix2) {
        if (matrix1.length != matrix2.length || matrix1[0].length != matrix2[0].length) {
            return null; 
        }

        int rows = matrix1.length;
        int cols = matrix1[0].length;
        int[][] result = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        return result;
    }

    // Function to multiply two matrices
    public static int[][] multiplyMatrices(int[][] matrix1, int[][] matrix2) {
        int rows1 = matrix1.length;
        int cols1 = matrix1[0].length;
        int rows2 = matrix2.length;
        int cols2 = matrix2[0].length;

        if (cols1 != rows2) {
            return null; // Matrices cannot be multiplied
        }

        int[][] result = new int[rows1][cols2];

        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                for (int k = 0; k < cols1; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                    // 1 2 3
                    // 4 5 6
                    //* 
                    // 2 0
                    // 1 2
                    // 0 1
                    //
                }
            }
        }
        return result;
    }

    public static void printMatrix(int[][] matrix) {
        if (matrix == null) {
            System.out.println("Matrix is null.");
            return;
        }
        for (int[] row : matrix) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] matrix1 = {{1, 2, 3}, {4, 5, 6}};
        int[][] matrix2 = {{7, 8, 9}, {10, 11, 12}};
        int[][] matrix3 = {{2,0},{1,2},{0,1}};

        System.out.println("Matrix 1:");
        printMatrix(matrix1);

        System.out.println("\nMatrix 2:");
        printMatrix(matrix2);

        System.out.println("\nMatrix 3:");
        printMatrix(matrix3);

        System.out.println("\nMatrix 1 + Matrix 2:");
        int[][] sum = addMatrices(matrix1, matrix2);
        printMatrix(sum);

        System.out.println("\nMatrix 1 * Matrix 3:");
        int[][] product = multiplyMatrices(matrix1, matrix3);
        printMatrix(product);

        System.out.println("\nMatrix 2 * Matrix 3:");
        int[][] product2 = multiplyMatrices(matrix2, matrix3);
        printMatrix(product2);
    }
}