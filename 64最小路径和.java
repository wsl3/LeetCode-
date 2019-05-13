import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] grid= new int[][]{{1,3,1},{1,5,1},{4,2,1}};
        System.out.println(s.minPathSum(grid));
    }
}

//直接在原数组上进行修改
class Solution {
    public int minPathSum(int[][] grid) {
        if(grid==null || grid.length==0){
            return 0;
        }

        int row = grid.length;
        int clo = grid[0].length;

        for(int i=1;i<row;i++){
            grid[i][0] += grid[i-1][0];
        }

        for(int j=1;j<clo;j++){
            grid[0][j] += grid[0][j-1];
        }
        //计算
        for(int i=1;i<row;i++){
            for(int j=1;j<clo;j++){
                grid[i][j] = Math.min(grid[i][j-1]+grid[i][j], grid[i-1][j]+grid[i][j]);
            }
        }

        return grid[row-1][clo-1];
    }
}



//5ms beat 85.85%
//class Solution {
//    public int minPathSum(int[][] grid) {
//        if(grid==null || grid.length==0){
//            return 0;
//        }
//
//        int row = grid.length;
//        int clo = grid[0].length;
//
//        //dp[x][y] 代表从(0,0)到(x,y)的最短距离
//        int[][] dp = new int[row][clo];
//        dp[0][0] = grid[0][0];
//
//        //初始化第一列
//        for(int i=1;i<row;i++){
//            dp[i][0] = dp[i-1][0] + grid[i][0];
//        }
//
//        //初始化第一行
//        for(int j=1;j<clo;j++){
//            dp[0][j] = dp[0][j-1] + grid[0][j];
//        }
//
//        //计算
//        for(int i=1;i<row;i++){
//            for(int j=1;j<clo;j++){
//                dp[i][j] = Math.min(dp[i][j-1]+grid[i][j], dp[i-1][j]+grid[i][j]);
//            }
//        }
//
//        return dp[row-1][clo-1];
//    }
//}