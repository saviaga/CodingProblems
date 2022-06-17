class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split() #split 
        s=[ elem[::-1] for elem in s] #reverse elements 
        res=" ".join(s) #join
	    
        
        return res