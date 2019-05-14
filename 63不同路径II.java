import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println();
    }
}

// 2ms beat 36%
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.length;
        int clo = obstacleGrid[0].length;
        int[][] dp = new int[row][clo];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < clo; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                } else if (i == 0 && j == 0) {
                    dp[i][j] = 1;
                } else if (i == 0) {
                    dp[i][j] = dp[i][j - 1];
                } else if (j == 0) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i][j-1];
                }
            }
        }
        return dp[row - 1][clo - 1];

    }
}
