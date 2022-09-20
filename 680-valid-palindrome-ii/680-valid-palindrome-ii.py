class Solution(object):
    def validPalindromecheck(self, s,start,end):
        while start < end:
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
        while start<end:
            if s[start]!=s[end]:
                return self.validPalindromecheck(s,start+1,end) or self.validPalindromecheck(s,start,end-1)
            start+=1
            end-=1
            
        return True
        