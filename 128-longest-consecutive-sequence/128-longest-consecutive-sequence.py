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
        #1. Store numbers in a set
        #2. go through the array and check if value-1 not in set (this means that current number is the start of a sequence)
            #do a while loop to get the secuence lenght
        #3. calculate the longest sequence so far
        #4. return sequence
        
        #{0:1,1:1,2:3,6:4,7:5,8:6}
        #Time O(n)
        #Space O(n)
        longest=0
        nums_dict = set(nums)
       
       
        for elem in nums:
            
            if elem-1 not in nums_dict:
                
                lenght = 1
                current = elem
                while current+1 in nums_dict:
                    lenght+=1
                    current+=1
                longest = max(longest,lenght)
        return longest
            
                