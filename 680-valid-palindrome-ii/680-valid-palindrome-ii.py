class Solution(object):
    def validPalindrome(self, s):
        print(s)
        """
        :type s: str
        :rtype: bool
        """
        def check_palindrome(s,i,j):
            while i < j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        start = 0
        end = len(s)-1       
        while start < end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return check_palindrome(s,start+1,end) or check_palindrome(s, start,end-1)
               

        return True
        