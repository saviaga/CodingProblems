class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverseStringHelper(start,end):
            if start==end:
                return
            
            elif start<end:
                s[start],s[end] = s[end],s[start]
           
                reverseStringHelper(start+1,end-1)

            
            
        start = 0
        end= len(s)-1
        reverseStringHelper(start,end)
        return s