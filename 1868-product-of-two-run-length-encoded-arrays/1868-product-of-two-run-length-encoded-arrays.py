class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        """
        :type encoded1: List[List[int]]
        :type encoded2: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        i =0
        j = 0
        res = []
        while i<len(encoded1) and j<len(encoded2):
            
            num1,freq1 = encoded1[i]
            num2,freq2 = encoded2[j]

            
            product = num1*num2
            freq = min(freq1,freq2)
            
            if not res or product!=res[-1][0]:
                res.append([product,freq])
                
            else:
                res[-1][1]+=freq
            
            encoded1[i][1]-=freq
            encoded2[j][1]-=freq
            
            if freq1== 0:
                i+=1
            if freq2== 0:
                j+=1
        return res
            
        
        
                
            
                
            
            
        
        
        
            