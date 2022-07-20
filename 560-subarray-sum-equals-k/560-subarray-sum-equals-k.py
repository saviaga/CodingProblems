class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        cs = 0
        dict_sum = {0:1}
        
        for i in range(len(nums)):           
            cs += nums[i];
            
            if (cs - k) in dict_sum: 
                count += dict_sum[cs - k]
            
            if cs in  dict_sum:
                dict_sum[cs]+=1
            else:
                dict_sum[cs] = 1

        return count
    
    #Time complexity : O(n)O(n). The entire numsnums array is traversed only once.

#Space complexity : O(n)O(n). Hashmap mapmap can contain up to nn distinct entries in the worst case.


                
                
            
            
        