public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        int[] nums = {1,3,5,6};
        Solution s = new Solution();
        System.out.println(s.searchInsert(nums, 4));
    }
}

class Solution {
    public int searchInsert(int[] nums, int target) {

        //特殊情况处理
        int length = nums.length;
        if (length == 0 || target < nums[0]) {
            return 0;
        } else if (target > nums[length - 1]) {
            return length;
        }

        //二分查找
        int left = 0, right = length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
