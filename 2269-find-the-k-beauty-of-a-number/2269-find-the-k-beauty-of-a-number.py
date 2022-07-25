class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        start = 0
        count = 0
        ls_num = str(num)
        
        for end in range(len(ls_num)-k+1):            
            n = int(ls_num[end:k+end])
           
            if n!=0 and num% n==0:  
                count+=1
           
        return count
    
   
    
    