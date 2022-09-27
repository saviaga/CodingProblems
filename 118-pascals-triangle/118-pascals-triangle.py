class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
          
        if numRows==1:return [[1]]
                
            
        inner_list = []
        past_row = self.generate(numRows-1)
        
        for j in range(0,len(past_row[-1])-1):
                
                inner_list.append(past_row[-1][j]+past_row[-1][j+1])

        full_row = [1] + inner_list + [1]
        past_row.append(full_row) 
       
      
        return past_row
        
        