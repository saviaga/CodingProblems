class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Input: [100,4,200,1,3,2]
        #Output: 4
        #Input: []
        #Output: 0
        
        #Input: [10]
        #Output: 1
        
        #Input: [0,1,2,2,6,7,8]
        #Output:4
        
        #Approach 1: "sort and sliding window"
        # Time: O(nlgn)
        # Space: O(1)
        
        #Approach 2: 
        #1. Store in a dictionary keys-> number values->index
        #2. go through the array and check if next value is in dict, if yes, count
        #3. start counter otherwise
        
        #{0:1,1:1,2:3,6:4,7:5,8:6}
        counter = 0
        longest=0
        nums_dict = set()
        for i in range(len(nums)):
            nums_dict.add(nums[i])
        
       
        for elem in nums:
            #check sequence
            
            if elem-1 in nums_dict:
                continue
            lenght = 1
            current = elem
            while current+1 in nums_dict:
                lenght+=1
                current+=1
            longest = max(longest,lenght)
        return longest
            
                