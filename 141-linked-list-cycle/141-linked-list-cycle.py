# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        fast = head
        
        
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
    
    #space complexity O(1)
    #Time complexity O(N+M) ~O(N) is the number of nodes
        
        
        