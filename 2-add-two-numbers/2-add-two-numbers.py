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
        
       
        
        
        
    def addTwoNumbers(self, l1, l2):
        curr_sum = l1.val + l2.val
        node_val=curr_sum % 10
        carry = curr_sum // 10
        node = ListNode(node_val)
        if any((l1.next, l2.next, carry)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += carry
            node.next = self.addTwoNumbers(l1, l2)    
        return node            
        
                
            
        