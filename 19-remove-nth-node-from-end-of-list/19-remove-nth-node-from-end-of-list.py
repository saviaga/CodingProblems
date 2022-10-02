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
        new_head = head
        if head.next ==None and n==1:
            return None
        
        lenght = 0
        curr =head
        while curr:
            lenght+=1
            curr = curr.next
        
        curr=head
        
        for _ in range((lenght-n-1)):
            curr = curr.next
        
        if lenght-n ==0:
            new_head = head.next
        elif curr.next:
                curr.next = curr.next.next
        else:
                curr.next = None
        return new_head 
        
        