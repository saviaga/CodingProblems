class Solution:

    def __init__(self, nums: List[int]):
        self.nums=collections.defaultdict(list)
        
        for i,value in enumerate(nums):
            self.nums[value].append(i)
       
         

    def pick(self, target: int) -> int:
      
        return random.choice(self.nums[target])    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)