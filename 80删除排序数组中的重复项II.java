import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println();
    }
}

// 1ms beat 100%
class Solution {
    public int removeDuplicates(int[] nums) {
        int i =0;
        for(int n: nums){
            if(i<2 || n!=nums[i-2]){
                nums[i] = n;
                i += 1;
            }
        }
        return i;
    }
}