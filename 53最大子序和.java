public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println(s.maxSubArray(nums));
    }
}

class Solution {
    public int maxSubArray(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int maxSum = nums[0];
        int nowSum = 0;
        for (int i = 0; i < nums.length; i++) {
            nowSum += nums[i];
            if (nowSum > maxSum) {
                maxSum = nowSum;
            }
            if (nowSum < 0) {
                nowSum = 0;
            }
        }
        return maxSum;
    }
}