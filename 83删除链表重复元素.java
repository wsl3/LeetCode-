import java.util.*;

public class test {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.climbStairs(6));
    }
}


//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
 }

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next == null){
            return head;
        }
        ListNode p = head;
        while(p.next!=null){
            ListNode q = p.next;
            while(q!=null && q.val==p.val){q=q.next;}
            if(q==null){
                p.next = null;
                break;
            }else{
                p.next = q;
                p = q;
            }
        }
        return head;
    }
}


