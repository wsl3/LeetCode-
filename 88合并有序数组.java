import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1, 2};

    }
}

//不创建新的数组, 利用nums1的空余位置, O(n)
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = (m--) + (n--) -1;
        int temp;
        while(m>=0 || n >=0){
            temp = (m>=0&&n>=0)?(nums1[m]>nums2[n]?nums1[m--]:nums2[n--]):(m>=0?nums1[m--]:nums2[n--]);
            nums1[index--] = temp;
        }
    }
}



// 1ms beat 99.34% 创建新的数组 temp[m+n], 最后把temp[]中的内容copy到nums1 --> O(n)
//class Solution {
//    public void merge(int[] nums1, int m, int[] nums2, int n) {
//        int[] temp = new int[m+n];
//        int index = 0, i=0,j=0;
//        int temp1;
//        while(i<m || j<n){
//            temp1 = (i<m&&j<n)?(nums1[i]>nums2[j]?nums2[j++]:nums1[i++]):(i<m?nums1[i++]:nums2[j++]);
//            temp[index++] = temp1;
//        }
//        for(i=0;i<(m+n);i++){
//            nums1[i] = temp[i];
//        }
//    }
//}






// 4ms beat 65%  先把nums2插入到nums1,nums1在排序
//class Solution {
//    public void merge(int[] nums1, int m, int[] nums2, int n) {
//        for(int i=m,j=0;j<n;i++,j++){
//            nums1[i] = nums2[j];
//        }
//
//        for(int i=0;i<nums1.length-1;i++){
//            for(int j=i+1;j<nums1.length;j++){
//                if(nums1[i]>nums1[j]){
//                    int temp = nums1[i];
//                    nums1[i] = nums1[j];
//                    nums1[j] = temp;
//                }
//            }
//        }
//    }
//}


