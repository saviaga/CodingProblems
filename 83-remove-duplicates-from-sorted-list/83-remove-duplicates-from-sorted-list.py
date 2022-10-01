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
        
        curNode = head
        while curNode:
            while curNode.next and curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
           
            curNode = curNode.next
        
        return head        