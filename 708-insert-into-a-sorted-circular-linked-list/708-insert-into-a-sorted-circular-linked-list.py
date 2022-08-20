"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        #if list is empty
        
        if head ==None:
            head=ListNode()
            head.val=insertVal
            head.next=head
            return head
            
        prev = head 
        curr = head.next
        node = ListNode(insertVal)  
        prev, curr = head, head.next
        
        while prev.next != head:
            # Case1: 1 <- Node(2) <- 3
            if node.val >= prev.val and node.val <= curr.val:
                break
            
            # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
                break
            
            prev, curr = prev.next, curr.next

        # Insert node.
        node.next = curr
        prev.next = node           
        
        return head

            
        