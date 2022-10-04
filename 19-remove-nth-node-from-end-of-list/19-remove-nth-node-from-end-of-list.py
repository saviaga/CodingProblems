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
        
        p1 = head
        counter = 0
        while p1:
            counter+=1
            p1 = p1.next
        
        position = (counter-n)-1
        if position <0:
            return head.next
        p1 = head
        for _ in range(position):
            p1 = p1.next
        p1.next = p1.next.next
        return head
        
        
            
            
            
            
            
        
        