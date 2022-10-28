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
    

        
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        
        def bst(head):
            if not head:
                return
            elif not head.next:
                return TreeNode(head.val)
                
            slow=head
            fast=head.next.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            tmp=slow.next
            slow.next=None
            root=TreeNode(tmp.val)
            root.left=bst(head)
            root.right=bst(tmp.next)
            return root
            
            
        return bst(head)