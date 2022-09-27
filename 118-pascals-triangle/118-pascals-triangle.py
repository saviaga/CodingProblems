class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def generatehelp(i):
          
            if i==numRows:
                return 
            
            inner_list = []
            past_row= self.dp[-1]
            for j in range(0,len(past_row)-1):                
                inner_list.append(past_row[j]+past_row[j+1])
            full_row = [1] + inner_list + [1]
            self.dp.append(full_row)
            return generatehelp(i+1)
        
        
        self.dp= [[1]]
        generatehelp(1)
        return self.dp
        
        