class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        if r == 0:
            return False
        c= len(matrix[0])
        
        start = 0
        end = r*c-1
        #We flatten the matrix
        #[1,2,5,7|10,11,16,20|23,30,34,60]
        # Find the middle. To find column middle // #colums
        #To fidn row middle % columns
        while start <= end:
            pivot = (start + end) //2
            curr_element = matrix[pivot//c][pivot%c]
            if target == curr_element:
                return True
            elif target < curr_element:
                end = pivot -1
            elif target > curr_element:
                start = pivot + 1
        return False
                
            