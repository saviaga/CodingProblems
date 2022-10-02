# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode()
        carry = 0
        curr = new_head
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            curr_sum = val1+val2+carry
            node_val = curr_sum %10
            carry = curr_sum //10
            curr.next = ListNode(node_val)
            curr= curr.next
            if l1: l1 = l1.next
            if l2: l2  = l2.next
            
        return new_head.next
            
        