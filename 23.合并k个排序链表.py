# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l =[]
        for i in lists:
        	while(i is not None):
        		l.append(i.val)
        		i = i.next
        l.sort()
        head = ListNode(0)
        p = head 

        for i in l:
        	q = ListNode(i)
        	p.next, p = q, q
        return head.next
