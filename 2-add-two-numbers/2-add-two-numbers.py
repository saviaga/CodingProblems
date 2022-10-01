# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #l1 = [2,4,3], l2 = [5,6,4]
        #carry =0
        #2+5=7 + carry(0)
        #4+6=0 + carry (0) 10 %10  carry 10//10
        #3+4 + carry(1) = 8
        #[7,0,8]-> reverse and return
        
        #l1 = [0], l2 = [5,6,4]
        #carry =0 
        #0+5 + carry(0) = 5
        #if one list is bigger just add the remaining elements to the result
        
        #l1 = [9,9,9,9,9,9,9], 
        #l2   [9,9,9,9]
        #      8 9 9 9 0 0 0 1          
        
        #result = 9+9 = 18/%10 -> 8 carry 18//10 - > 1
        #result 9=8, 9 carry 1
        
       
        
        carry = 0
        sum_node = ListNode()
        new_head = sum_node
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curr_sum = val1 + val2 + carry
            
            node_val = curr_sum%10
            carry = curr_sum//10
            sum_node.next = ListNode(node_val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sum_node =sum_node.next
       
        
        return new_head.next
            
        
                
            
        