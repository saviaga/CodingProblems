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
        
        node = head
        array = []
        while node:
            array.append(node.val)
            node = node.next
        def arrayToBST(array, l, r):
            if l > r:
                return
            m = (l + r) // 2
            BST = TreeNode(array[m])
            BST.left = arrayToBST(array, l, m - 1)
            BST.right = arrayToBST(array, m + 1, r)
            return BST
        return arrayToBST(array, 0, len(array) - 1)