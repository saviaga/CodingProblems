class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        
        opening = 0
        to_valid = 0
        for elem in s:
            if elem =='(': 
                opening+=1
            else:
                opening-=1
            if opening ==-1:
                to_valid+=1
                opening+=1
            
        return to_valid+opening
                    
        