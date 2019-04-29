public class Main {

    public static void main(String[] args) {
        Solution s = new Solution();
        String string = "he wor ";
        System.out.println(s.lengthOfLastWord(string));
    }
}

class Solution {
    public int lengthOfLastWord(String s) {
        if(s.length()==0){
            return 0;
        }
        int i=s.length()-1;
        while(i>=0 && s.charAt(i)==' '){i--;}
        if(i<0){
            return 0;
        }
        int lastIndex = i--;
        for(;i>=0;i--){
            if(s.charAt(i)==' '){
                break;
            }
        }
        return lastIndex-i;
    }
}