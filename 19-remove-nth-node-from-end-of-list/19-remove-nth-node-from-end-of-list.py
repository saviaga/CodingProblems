# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0,head)
        
        first = head 
        num_elem = 0
        while first:
            num_elem+=1
            first = first.next
        
        num_elem -=n
        first = dummy
        while num_elem > 0:
            num_elem-=1
            first = first.next
            
        first.next = first.next.next
        return dummy.next
        