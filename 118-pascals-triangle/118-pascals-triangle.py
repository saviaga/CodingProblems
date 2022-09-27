class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def generatehelp(cdp, i):
          
            if i==numRows:
                return dp
            
            inner_list = []
            past_row = cdp[-1]
            for j in range(0,len(past_row)-1):
                
                inner_list.append(past_row[j]+past_row[j+1])

            full_row = [1] + inner_list + [1]
          
            cdp.append(full_row)
            return generatehelp(cdp,i+1)
        
        
        dp = [[1]]
        generatehelp(dp,1)
        return dp
        
        