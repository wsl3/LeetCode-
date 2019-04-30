import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.addBinary("1010","1011"));
    }
}

// 4ms , beat 90%
class Solution {
    public String addBinary(String a, String b) {
        StringBuffer sb = new StringBuffer();
        int index_a = a.length()-1;
        int index_b = b.length()-1;
        int temp = 0;
        while(index_a>=0 || index_b>=0 || temp==1){
            int value_a = index_a>=0?(a.charAt(index_a)=='1'?1:0):0;
            int value_b = index_b>=0?(b.charAt(index_b)=='1'?1:0):0;
            int sum = value_a + value_b + temp;
            switch(sum){
                case 0:sb.append("0");break;
                case 1:sb.append("1");temp=0;break;
                case 2:sb.append("0");temp=1;break;
                case 3:sb.append("1");temp=1;break;
            }
            index_a--;
            index_b--;
        }
        return sb.reverse().toString();
    }
}


//a nice way: 5ms, beat 74%
//class Solution {
//    public String addBinary(String a, String b) {
//        StringBuffer sb = new StringBuffer();
//        int index_a = a.length()-1;
//        int index_b = b.length()-1;
//        int temp = 0;
//        while(index_a>=0 || index_b>=0 || temp==1){
//            int value_a = index_a>=0?(a.charAt(index_a)=='1'?1:0):0;
//            int value_b = index_b>=0?(b.charAt(index_b)=='1'?1:0):0;
//            int sum = value_a + value_b + temp;
//            switch(sum){
//                case 0:sb.insert(0,"0");break;
//                case 1:sb.insert(0,"1");temp=0;break;
//                case 2:sb.insert(0,"0");temp=1;break;
//                case 3:sb.insert(0,"1");temp=1;break;
//            }
//            index_a--;
//            index_b--;
//        }
//        return sb.toString();
//    }
//}



// 8ms beat 32%(cry!!!)
//class Solution {
//    public String addBinary(String a, String b) {
//        int index_a = a.length() - 1;
//        int index_b = b.length() - 1;
//        String result = "";
//        int temp = 0;
//        for (; index_a >= 0 && index_b >= 0; index_a--, index_b--) {
//            if (a.charAt(index_a) == '1' && b.charAt(index_b) == '1') {
//                result = (temp == 1 ? "1" : "0") + result;
//                temp = 1;
//            } else if ((a.charAt(index_a) == '1' && b.charAt(index_b) == '0') || (a.charAt(index_a) == '0') && b.charAt(index_b) == '1') {
//                result = (temp == 1 ? "0" : "1") + result;
//            } else {
//                result = (temp == 1 ? "1" : "0") + result;
//                temp = 0;
//            }
//        }
//        if (index_a == -1 && index_b == -1) {
//            return (temp == 1 ? "1" : "") + result;
//        }
//        String temp_str;
//        int temp_index;
//        if (a.length() > b.length()) {
//            temp_str = a;
//            temp_index = index_a;
//        } else {
//            temp_str = b;
//            temp_index = index_b;
//        }
//        while (temp_index >= 0) {
//            if (temp_str.charAt(temp_index) == '1') {
//                result = (temp == 1 ? "0" : "1") + result;
//            } else {
//                result = (temp == 1 ? "1" : "0") + result;
//                temp = 0;
//            }
//            temp_index--;
//        }
//
//        return (temp==1?"1":"")+result;
//    }
//}