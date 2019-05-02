import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.mySqrt(2147395599));
    }
}

// 6ms beat 93%
//牛顿迭代法：https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
// Note: (a + b)/2 >= sqrt(ab)
class Solution {
    public int mySqrt(int x) {
        long result = x;
        while(result*result > x){
            result = (result + x/result)/2;  // result = (int)sqrt(x)
        }
        return (int)result;
    }
}



// beat 5%
//class Solution {
//    public int mySqrt(int x) {
//        if (x <= 1) {
//            return x;
//        }
//        long left = 1, right = x;
//        long mid = (left + right) / 2;
//        while (!(mid * mid <= x && (mid + 1) * (mid + 1) > x)) {
//            if(mid*mid>x){
//                right = mid;
//            }else{
//                left = mid;
//            }
//            mid = (left+right)/2;
//            System.out.println(mid);
//        }
//        return (int)mid;
//    }
//}



// timeout!
//class Solution {
//    public int mySqrt(int x) {
//        if(x<=1){
//            return x;
//        }
//        int i;
//        for(i=1;i<x;i++){
//            if((i*i==x) || (i*i<x && ((i+1)*(i+1))>x)){
//                break;
//            }
//        }
//        return i;
//    }
//}