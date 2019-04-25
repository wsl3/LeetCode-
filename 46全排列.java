import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<List<Integer>> t = new ArrayList<>();
        int[] nums = {1,2,3};
        Solution s = new Solution();
        t = s.permute(nums);

        for(int i=0;i<t.size();i++){
            for(int j=0;j<t.get(i).size();j++){
                System.out.print(t.get(i).get(j));
                System.out.print(" ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void test(List<Integer> test) {
        test.add(1);
        test.add(2);
    }
}

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }
        helper(0, nums, result);


        return result;
    }

    public void helper(int index, int[] nums, List<List<Integer>> result) {
        if (result.isEmpty()) {
            List<Integer> temp = new ArrayList<>();
            temp.add(nums[index]);
            result.add(temp);
        } else {
            int len = result.size();
            int len2 = result.get(0).size();
            for (int i = 0; i < len; i++) {
                for (int j = 0; j <= len2; j++) {
                    List<Integer> temp = deepCopy(result.get(i));
                    temp.add(j, nums[index]);
                    result.add(temp);
                }
            }
            result.removeIf(next -> next.size() == len2);
        }

        if(index<(nums.length-1)){
            helper(index+1,nums,result);
        }
    }
    public List<Integer> deepCopy(List<Integer> t){
        List<Integer> s = new ArrayList<>();
        for(int i=0;i<t.size();i++){
            s.add(t.get(i));
        }
        return s;
    }
}