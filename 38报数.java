public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.countAndSay(6));
    }
}

class Solution {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        int quality = 0, i = 0;
        String result = "";
        String str = countAndSay(n - 1);
        char temp = str.charAt(0);
        while (i < str.length()) {
            if (str.charAt(i) == temp) {
                quality++;
                i++;
            } else {
                result += (quality + String.valueOf(str.charAt(i - 1)));
                temp = str.charAt(i);
                quality = 0;
            }
        }
        result += (quality+String.valueOf(str.charAt(i-1)));
        return result;
    }
}