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
        
        fast = dummy 
        slow = dummy
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n+1): 
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next  
        return dummy.next
        