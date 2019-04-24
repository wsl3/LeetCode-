class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int temp, i, j;

        // ‘/’反转
        for (i = 0; i < n-1; i++) {
            for (j = 0; j < (n - i-1); j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[n-1-j][n-1-i];
                matrix[n-1-j][n-1-i] = temp;
            }
        }
        // 中轴线反转
        for (i = 0; i < n / 2; i++) {
            for (j = 0; j < n; j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[n-i-1][j];
                matrix[n-i-1][j] = temp;
            }
        }
    }
}
