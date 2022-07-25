class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_dic = {0:-1}
        
        total = 0
        for i, n in enumerate(nums):
            total+=n
            remainder = total%k
            if remainder not in remainder_dic:
                remainder_dic[remainder]  = i #we store index
            elif i - remainder_dic[remainder] > 1: #if at least 2 elems
                return True
        return False
            
            
            
        
        