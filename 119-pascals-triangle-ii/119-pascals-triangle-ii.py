class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        
        if rowIndex ==0:
            return [1]

            
        last_row = self.getRow(rowIndex-1)
        inner_list = []
            
        for i in range(0,len(last_row)-1):
            inner_list.append(last_row[i]+ last_row[i+1])
                
        full_row = [1] + inner_list + [1]
     
        return full_row
        
        
        
        