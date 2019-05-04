import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1,8,6,2,5,4,8,3,7};
        System.out.println(s.maxArea(nums));
    }
}

//双指针法   2ms beat 100%
class Solution {
    public int maxArea(int[] height) {

        if(height.length==2){
            return height[0]>height[1]?height[1]:height[0];
        }
        int i=0,j=height.length-1;
        int max = 0;
        int temp, flag=0;
        int temp_index;
        while(i<j){
            if(height[i]<height[j]){
                temp = height[i]*(j-i);
                flag = 0;
            }else{
                temp = height[j]*(j-i);
                flag = 1;
            }
            max = max>temp?max:temp;


            if(flag==0){
                temp_index = i+1;
                while(temp_index<j && height[temp_index]<height[i]){temp_index++;}
                if(temp_index==j){
                    break;
                }
                i=temp_index;
            }else{
                temp_index = j-1;
                while(temp_index>i && height[temp_index]<height[j]){temp_index--;}
                if(temp_index==i){
                    break;
                }
                j=temp_index;
            }

        }

        return max;
    }
}



// 暴力法 390ms beat 33%
//class Solution {
//    public int maxArea(int[] height) {
//        int max = height[0]>height[1]?height[1]:height[0];
//        int temp;
//        for(int i=0;i<height.length-1;i++){
//            for(int j=i+1;j<height.length;j++){
//                temp = height[i]>height[j]?height[j]:height[i];
//                max = (temp*(j-i))>max?(temp*(j-i)):max;
//            }
//        }
//        return max;
//    }
//}


