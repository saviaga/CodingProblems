# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findsize(self,head):
          
        end =0
        curr = head
        
        while curr:
            curr = curr.next
            end+=1
        return end
        
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        def helper(l,r,head):
            if l > r:
                return None
            mid = (l + r) //2
         
            counter = 0
            node = head
            #arrive to mid
            while counter<mid:
                node = node.next
                counter+=1
               
 
            root = TreeNode(node.val) 
          
            root.left = helper(l,mid-1,head)
            root.right = helper(mid+1,r,head)
            return root
        
       
        return helper(0, self.findsize(head)-1,head)
        