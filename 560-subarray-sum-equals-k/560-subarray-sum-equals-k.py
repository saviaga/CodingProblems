class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        
        cs = 0
        
        dic_cs= {0:1}
        
        
        for elem in nums:
            cs+=elem
            
            if (cs-k) in dic_cs:
                count+=dic_cs[cs-k]
                
            if cs in dic_cs:
                dic_cs[cs] += 1
            else:
                dic_cs[cs] = 1
        
        print(dic_cs)
        return count