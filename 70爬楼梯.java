import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.climbStairs(6));
    }
}

// beat 100%!!!
//n:1 2 3 4 5 6
//  1 2 3 5 8 13
//计算斐波拉契数列
class Solution {
    public int climbStairs(int n) {
        if(n<3){
            return n;
        }
        int x = 2;
        int result = 3;
        for(int i=3;i<n;i++){
            int temp = x+result;
            x = result;
            result = temp;
        }
        return result;
    }
}

// 直接递归 timeout!
//class Solution {
//    public int climbStairs(int n) {
//        if(n<3){
//            return n;
//        }
//        return climbStairs(n-1)+climbStairs(n-2);
//    }
//}


