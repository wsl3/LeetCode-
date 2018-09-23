# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if(p is not None and p.next is not None):
        	temp = p.next
        	p.next = temp.next
        	temp.next = p
        	head = temp
        else:
        	return head

        while(p.next is not None and p.next.next is not None):
        	temp = p.next.next
        	p.next.next = temp.next
        	temp.next = p.next
        	p.next = temp 
        	p = p.next.next
        return head

