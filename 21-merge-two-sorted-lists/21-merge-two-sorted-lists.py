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
            

        while list1 and list2:
            if list1.val < list2.val:
                curr_node.next = list1
                
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        
        if list1: 
            curr_node.next = list1
          
        elif list2:
            curr_node.next = list2
           
               
        return new_head.next
                
        