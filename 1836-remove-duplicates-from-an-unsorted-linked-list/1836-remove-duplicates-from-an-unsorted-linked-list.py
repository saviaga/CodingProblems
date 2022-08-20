# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        if head==None:
            return []
        
        
        curr = head
        elems = defaultdict(int)
        
        #save in dictionary
        while curr!=None:         
                elems[curr.val]+=1
                curr = curr.next
      
        #check those with value>=2 and delete them
        dummy = ListNode()
        curr = dummy   
        while head:
            if elems[head.val] == 1:
                curr.next = head
                curr = curr.next
            head = head.next 
        curr.next = None
        
        return dummy.next
            
        