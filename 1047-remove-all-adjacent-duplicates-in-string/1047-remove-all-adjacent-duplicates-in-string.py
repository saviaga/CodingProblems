class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for elem in s:
            if stack and elem == stack[-1]:
                stack.pop()
            else:
                stack.append(elem)
        return "".join(stack)
        
        #Time complexity : \mathcal{O}(N)O(N), where N is a string length.
#Space complexity : \mathcal{O}(N - D)O(N−D) where D is a total length for all duplicates.
        
        