class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for row in accounts:
            wealth = 0
            for col in row:
                wealth+=col
            max_wealth = max(max_wealth,wealth)
        return max_wealth
            