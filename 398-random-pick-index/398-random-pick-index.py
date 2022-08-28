class Solution:

    def __init__(self, nums: List[int]):
        self.dic_idx=collections.defaultdict(list)
        for i,value in enumerate(nums):
            self.dic_idx[value].append(i)
         
    def pick(self, target: int) -> int:
        return random.choice(self.dic_idx[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)