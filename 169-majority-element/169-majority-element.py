class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[2,2,1,1,1,2,2]
        #.    ^
        #count=1
        #candidate=0
        count = 0
        candidate = 0
        for elem in nums:
            if count==0:
                candidate =elem
                count+=1
            elif elem!=candidate:
                count-=1
            else:
                count+=1
        return candidate
                
            
                
#Time Complexity O(n) -> iterate over the nums array one time

#Space complexity O(1)-> stores constant aditional memory