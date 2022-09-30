# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head:
            return head
        curr = head
        
        while curr!=None and curr.next!=None:
           
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
                   
        return head
        