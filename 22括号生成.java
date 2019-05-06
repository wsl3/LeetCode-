import java.lang.reflect.Array;
import java.util.*;


public class Main{
    public static void main(String[] args){

    }
}


// 3ms beat 85%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        traceback(result,"(",1,0,n);
        return result;

    }
    public void traceback(List<String> result,String str,int left,int right,int n){
        if(str.length() == 2*n){
            result.add(str);
        }
        // 左括号个数<n时才能添加左括号
        if(left<n){
            traceback(result,str+"(",left+1,right,n);
        }
        //左括号个数>右括号个数时 才能添加右括号
        if(right<left){
            traceback(result,str+")",left,right+1,n);
        }
    }
}