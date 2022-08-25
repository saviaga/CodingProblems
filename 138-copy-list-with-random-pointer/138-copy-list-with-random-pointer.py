"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head==None:
            return head
        
        curr = head
        #first pass insert the new_nodes A->A'
        while curr:
            new_node = Node(curr.val)
            new_node.next =curr.next
            curr.next = new_node
            curr = new_node.next
            
        
            
        #link the random pointers to the new nodes
        curr= head
        while curr:
            #the cloned random
            curr.next.random = curr.random.next if curr.random else None 
            curr = curr.next.next
        
              
        #unlink the old ones 
        old = head# A->B->C
        new = head.next# A'->B'->C'
        new_head = head.next
        
        while old:
            old.next = new.next
            new.next = old.next.next if old.next else None
            old = old.next
            new=new.next
        return new_head
     
            
        
        
        
        