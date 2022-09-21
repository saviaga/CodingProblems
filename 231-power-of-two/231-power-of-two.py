class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return n % 2 == 0 and self.isPowerOfTwo(n//2)