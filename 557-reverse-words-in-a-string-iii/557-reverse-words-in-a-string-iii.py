class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        s=s[::-1]  #reverse string
        s=s.split() #split it
        s=s[::-1] #reverse elements again

        res=" ".join(s) #join
        return res
        
        