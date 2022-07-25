class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        k=3
        count =0
        
        for end in range(len(s)-k+1):
            sub = s[end:k+end]
            
            #check dubplicates, 
            set_sub = set(sub)
            
            #if not duplicates count
            if len(sub) == len(set(sub)):
                count+=1
        return count
            
            
            