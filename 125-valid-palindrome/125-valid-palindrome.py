class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        
        while start <= end:
            while not s[start].isalnum() and start<end:
                start+=1
                
            if not s[end].isalnum() and end>start:
                end-=1
                continue
            if s[start].lower() !=s[end].lower():
                return False
            start+=1
            end-=1
        return True