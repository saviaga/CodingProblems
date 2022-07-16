class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        start = 0
        end = len(s)-1
        
        while start < end:
            
            while start < end and not s[start].isalnum():                
                start+=1
            while start < end and not s[end].isalnum():               
                end-=1
            if s[start].lower()==s[end].lower(): 
                start+=1
                end-=1
            else:
                return False
        return True
                
        