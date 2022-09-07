class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count=0
        dic_nums = defaultdict(int)
        
        for i in range(len(nums)): 
            complement = k - nums[i]
            if dic_nums[complement]>0:
                count+=1
                dic_nums[complement]-=1
            else:
                dic_nums[nums[i]] = dic_nums.get(nums[i],0)+1
                
                
       
                
        return count
        