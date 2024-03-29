class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for x in range(len(text1)+1)] for y in range(len(text2)+1)]
       
        
        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                
                #to options, is equal of the value so far without them, plus one one,
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    #it is not equal then just keep the count of the maximum so far
               
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
                
        
        