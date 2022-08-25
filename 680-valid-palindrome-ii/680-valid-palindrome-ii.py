class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        def valid_palindromehelper(s,start,end):
            while start<=end:
                if s[start]==s[end]:
                    start+=1
                    end-=1
                else: 
                    return False
            return True
            
        start = 0
        end= len(s)-1
        while start<=end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                left = valid_palindromehelper(s,start+1,end)
                right = valid_palindromehelper(s,start,end-1)
                return left or right
        return True
            
            

        