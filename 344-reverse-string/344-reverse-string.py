class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        def reverseStringHelper(start,end,s):
            if start>end:
                return
            else:
                s[start],s[end] = s[end],s[start]
                return reverseStringHelper(start+1,end-1,s)
            
                
            
        return reverseStringHelper(0,len(s)-1,s)