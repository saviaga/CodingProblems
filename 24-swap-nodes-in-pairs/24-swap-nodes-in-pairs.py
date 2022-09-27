# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #1->2    ->3->4
        #^
        #2-><-1
        
        if head ==None or head.next == None:
            return head
        
        first_node = head
        second_node = head.next
        

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        return second_node 
        
        
           
        