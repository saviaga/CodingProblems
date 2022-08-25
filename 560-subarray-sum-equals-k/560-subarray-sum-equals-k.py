class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count= 0
        cs= 0
        dic_cs={0:1}
        for elem in nums:
            cs+=elem
            if (cs-k) in dic_cs:
                count+=dic_cs[cs-k]
            dic_cs[cs]= dic_cs.get(cs, 0) + 1
         
        return count
