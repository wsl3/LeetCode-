import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();
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

// 1ms beat 92.64%  递归！！！
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p==null && q==null){
            return true;
        }else if (p!=null && q!=null){
            return (p.val==q.val) && isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        }else{
            return false;
        }

    }
}


