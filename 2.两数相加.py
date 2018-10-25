# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p, flag = head, 0
       	while l1 is not None or l2 is not None:
       		x1 = l1.val if l1 is not None else 0
       		x2 = l2.val if l2 is not None else 0
       		temp = ListNode((x1+x2+flag)%10)
       		flag = 1 if (x1+x2+flag)>9 else 0
       		p.next, p = temp, temp
       		l1 = l1.next if l1 is not None and l1.next is not None else None
       		l2 = l2.next if l2 is not None and l2.next is not None else None
       	if flag == 1:
       		p.next = ListNode(1)
       	return head.next

if __name__ == "__main__":

        
