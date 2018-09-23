# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        tail = head
        p, q = l1, l2
        while(p and q):
        	if p.val <= q.val:
        		tail.next, p = p, p.next
        		tail = tail.next
        		tail.next = None
        	else:
        		tail.next, q = q, q.next
        		tail = tail.next 
        		tail.next = None
        if(p is None):
        	tail.next = q
        else:
        	tail.next = p
        head = head.next
        return head