# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lenght = 0
        arr = []
        while head:
            arr.append(head) 
            head = head.next
            

        return arr[len(arr)/2]
            
        