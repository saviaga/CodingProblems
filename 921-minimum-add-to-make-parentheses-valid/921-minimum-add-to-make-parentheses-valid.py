class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        
        opening = 0
        to_valid = 0
        for elem in s:
            if elem =='(': 
                opening+=1
            else:
                
                if opening >0:
                    opening-=1
                else:
                    to_valid+=1
                    
        
        print('f')
        return to_valid+opening
                    
        