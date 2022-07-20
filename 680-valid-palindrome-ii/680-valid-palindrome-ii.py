class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_removing_one(s,i,j):
            
            while i <=j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        
        
        start = 0
        end = len(s)-1
        
        while start <=end:
            if s[start] == s[end]:
                start+=1
                end-=1
               
            else:
                return check_removing_one(s,start+1,end) or check_removing_one(s,start,end-1)
        return True
            