class Solution:
    #[-1,0,1,2,-1,-4]
    #[-1,-1,0,1,2]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dups = set()
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in dups:
                dups.add(nums[i])
                for j in range(i+1,len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in seen and seen[complement] == i:
                        numbers = [nums[i], nums[j], complement]
                        numbers.sort()
                        res.add(tuple(numbers))
                    seen[nums[j]] = i
                  
        return res        