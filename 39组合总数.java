import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(Character.getNumericValue('6'));
    }
}

//10ms beat 78%
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> nums = new ArrayList<>();
        traceback(result, candidates, target, nums, 0);
        return result;
    }

    public void traceback(List<List<Integer>> result, int[] candidates, int target, List<Integer> nums, int index) {
        if (target == 0) {
            result.add(nums);
            return;
        }
        if(target < candidates[index]){
            return;
        }
        for (int i = index; i < candidates.length&&candidates[i]<=target; i++) {
            List<Integer> temp = new ArrayList<>(nums);
            temp.add(candidates[i]);
            traceback(result,candidates,target-candidates[i],temp,i);
        }
    }
}