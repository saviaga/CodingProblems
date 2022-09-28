# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return 
        
        
        new_head = ListNode()
        curr_node = new_head
            
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.val < head2.val:
                curr_node.next = head1
                curr_node = curr_node.next
                head1 = head1.next
            else:
                curr_node.next = head2
                curr_node = curr_node.next
                head2 = head2.next
        
        while head1:
            
            curr_node.next = head1
            curr_node = curr_node.next
            head1 = head1.next
        while head2:
           
            curr_node.next = head2
            curr_node = curr_node.next
            head2 = head2.next
            
            
               
        return new_head.next
                
        