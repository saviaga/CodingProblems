class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def isPowerOfTwoHelper(result):
            
            if n == result:
                return True 
            if  result > n:
                return False
            result *=2
            return isPowerOfTwoHelper(result)
           
        
        result = 1
        return isPowerOfTwoHelper(result)