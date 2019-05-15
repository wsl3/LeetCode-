import java.lang.reflect.Array;
import java.util.*;


public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        ListNode head = new ListNode(1);
        ListNode t1 = new ListNode(4);
        ListNode t2 = new ListNode(3);
        head.next = t1;
        t1.next = t2;
        s.partition(head,3);
        System.out.println();
    }
}


class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
    }
}

// 2ms beat 50%
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode res = new ListNode(0);
        res.next = head;

        ListNode left = res;
        ListNode prev = res;
        ListNode curr = res.next;

        while(curr != null){
            if(curr.val < x){
                if(left.next==curr){
                    left = curr;
                    prev = curr;
                    curr = prev.next;
                }else{
                    prev.next = curr.next;
                    curr.next = left.next;
                    left.next = curr;
                    left = curr;
                    curr = prev.next;
                }
                continue;
            }
            while(curr!=null && curr.val >= x){ prev=curr;curr=curr.next;}
            if(curr == null){
                break;
            }
        }
        return res.next;
    }
}