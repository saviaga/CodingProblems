class Solution(object):
    def validatepalindrome(self,s,start,end):

            while start<=end:
                if s[start]==s[end]:
                    start+=1
                    end-=1
                else:
                    return False
            return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
    
    
        start = 0
        end = len(s)-1
        
        while start<=end:
            
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                #look withouth elem in right
                left = self.validatepalindrome(s,start+1,end)
                right = self.validatepalindrome(s,start,end-1)
                #look without elem in left
                return left or right
                
        return True
            
            