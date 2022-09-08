class Solution(object):
    
    def validPalindromeHelper(self, start,end,s):
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
        
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        start = 0
        end = len(s)-1
        
        while start<=end:
            if s[start]!=s[end]:
                return self.validPalindromeHelper(start+1,end,s) or self.validPalindromeHelper(start,end-1,s)

            start+=1
            end-=1
        return True
            
            
            
        
        