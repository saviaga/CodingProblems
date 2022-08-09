class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        subset_sum = sum(nums)//2
        n = len(nums)
        
        #construct dp
        dp = [[False for x in range(subset_sum + 1)] for y in range(n + 1)]
        dp[0][0] = True
        for i in range(1,n+1):
            for j in range(subset_sum + 1):
                
               
                if nums[i-1] > j: #if i cannot include it, then don't
                    dp[i][j] = dp[i-1][j]
                    
                elif nums[i-1] == j:
                    dp[i][j] = True
                else:
                    #not include it or include it
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    
                    

        return  dp[n][subset_sum]
        