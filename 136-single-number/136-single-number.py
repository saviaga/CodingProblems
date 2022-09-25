class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #if we take XOR of zero and some bit, it will return that bit
        # a XOR 0=a
        # a XOR a=0
        a= 0 
        for elem in nums:
            a = a^elem
        return a
            
