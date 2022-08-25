class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainder_dic = {0:-1}
        
        total = 0
        for i, n in enumerate(nums):
            total+=n
            
            remainder = total%k
           
            if remainder not in remainder_dic: #remainder not in dic
                remainder_dic[remainder]  = i #we store index
            
            #remainder in dic, check that size>2
            elif i - remainder_dic[remainder] > 1: #if at least 2 elems
                return True
            
        return False
            
        