class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #[3,2,3]  -> 2
        #[1] -> 
        #[1,2] -> [1,2]
        
        #approach 1:  hashmap
        # got throught each element store in hashmap(eg.3:2)
        #got throgh the hashmap and check if value >n/3 if yes then add to the resulting list
        #Time O(N)
        #Space O(N) depends on the # of different elems in nums
        hashmap = {}
        result = []
        for elem in nums:
            if elem in hashmap.keys():
                hashmap[elem]+=1
            else:
                hashmap[elem]=1
        
        for k,v in hashmap.items():
            if v > len(nums)//3:
                result.append(k)
        return result