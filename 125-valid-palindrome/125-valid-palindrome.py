class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        #pointer start, end
        #first check if pointer start is alpha, if it is not, move it forward
        #first check if pointer end is alpha, if it is not, move it back
        #if both are alpha, then first convert to lower and compare
        #if they are different then return false
        #keep comparing until start<=end
        
        start=0
        end=len(s)-1
        
        while start<=end:
            if not s[start].isalnum():
                start+=1
                continue
            elif not s[end].isalnum():
                end-=1
                continue
            #condition 1
            elif s[start].lower() != s[end].lower():
                    return False
            
            start+=1
            end-=1
        return True