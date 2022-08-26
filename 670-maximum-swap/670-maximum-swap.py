class Solution:
    def maximumSwap(self, num: int) -> int:
        
        #2:i0, 7:i1,3:i2, 6:i3  
        numsl = [elem for elem in str(num)]
        dic_idx={}
        
        for i in range(len(numsl)):
            dic_idx[int(numsl[i])] = i
            
        for i in range(len(numsl)):
            for j in reversed(range(10)):
                current = int(numsl[i])
                if j > current and j in dic_idx and dic_idx[j]>i:
                    numsl[i],numsl[dic_idx[j]] =numsl[dic_idx[j]],numsl[i]
                   
                    return int("".join(numsl))
        return num
                
            
        
                    
        