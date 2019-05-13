import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.numTrees(3));
    }
}

// 0ms beat 100%
class Solution {
    public int numTrees(int n) {
        int[] dp = new int[n+1];
        int temp;
        dp[0] = 0;
        dp[1] = 1;

        for(int i=2;i<n+1;i++){
            for(int j=1;j<=i;j++){
                if(j==1 || j==i){
                    temp = dp[i-1];
                }else{
                    temp = dp[j-1] * dp[i-j];
                }
                dp[i] += temp;
            }
        }


        return dp[n];
    }
}