class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
             return []
        else:
            res = [[1]]

        new_elem = []
        for i in range(numRows-1):         
            curr_elem = res[i]
            new_elem = []
            new_elem.append(curr_elem[0])
            for e in range(1,len(curr_elem)):
                new_elem.append(curr_elem[e]+curr_elem[e-1])
                e+=1
            new_elem.append(curr_elem[-1])
            res.append(new_elem)                 
        return res
     
     