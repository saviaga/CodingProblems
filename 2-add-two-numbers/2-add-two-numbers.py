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
        
       
        
        
        
        def addTwoNumbersHelper(node, v1,v2,carry_val):
            #print(node.val,v1,v2,carry_val)
            if not v1 and not v2 and not carry_val:
                return
            
            
            val1 = v1.val if v1 else 0
            val2 = v2.val if v2 else 0
            curr_suma = val1 + val2 + carry_val

            node_val = curr_suma%10
            carry_val = curr_suma//10
            node.next = ListNode(node_val)
            v1 = v1.next if v1 else None
            v2 = v2.next if v2 else None
            node =node.next

            return addTwoNumbersHelper(node,v1,v2,carry_val)
        
        
        sum_node = ListNode()
        new_head = sum_node
        addTwoNumbersHelper(sum_node,l1,l2,0)
        return new_head.next
            
        
                
            
        