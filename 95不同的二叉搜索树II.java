import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println();
    }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

//递归 beat 68%
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if(n==0){
            List<TreeNode> res = new ArrayList<>();
            return res;
        }
        return helper(1,n);
    }

    public List<TreeNode> helper(int begin, int end){
        List<TreeNode> res = new ArrayList<>();
        if(begin>end){
            res.add(null);
            return res;
        }

        for(int root=begin;root<=end;root++){
            List<TreeNode> left = helper(begin, root-1);
            List<TreeNode> right = helper(root+1, end);

            for(int i=0;i<left.size();i++){
                for(int j=0;j<right.size();j++){
                    TreeNode temp = new TreeNode(root);
                    temp.left = left.get(i);
                    temp.right = right.get(j);
                    res.add(temp);
                }
            }
        }
        return res;
    }
}