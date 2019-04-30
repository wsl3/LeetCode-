import java.util.*;

public class test {
    public static void main(String[] args){
        Solution s = new Solution();
        int[] test = {9,9,9};
        int[] result = s.plusOne(test);
        for(int i=0;i<result.length;i++){
            System.out.print(result[i]+" ");
        }
        System.out.println();
    }
}

class Solution {
    public int[] plusOne(int[] digits) {
        int temp = 1;
        for(int i=digits.length-1;i>=0;i--){
            digits[i] += temp;
            if(digits[i]>=10){
               digits[i] = digits[i] % 10;
               temp = 1;
            }else{
                temp = 0;
            }
        }
        if(temp == 0){
            return digits;
        }
        return insert(digits);
    }
    public int[] insert(int[] digits){
        int length = digits.length;
        int[] temp = new int[length+1];
        temp[0] = 1;
        for(int i=1;i<=length;i++){
            temp[i] = digits[i-1];
        }
        return temp;
    }
}