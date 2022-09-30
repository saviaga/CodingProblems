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
        #U: There is no null, hence that is a cycle
        # if we arrive again to the same element there is a cyle
        #If we find a null there is no cycle
        #if empty there is a cycle
        
        #M: Fast and Low Pointer
        #if they at some point meet, there is a cycle
        #if at some point we reach null with either pointer there isn't a cycle
        
        #P: While both pointers are different continue moving pointers, or while both pointers are different of null
        # if pointers are equal return true
        #if any pointer is null return false
        
        if not head: 
            return False
        
        slow = head
        fast = head.next
        
        while slow!=fast:
            
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
         
            
        return True
        
        
        
        