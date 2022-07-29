class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for row in range(len(accounts)):
            customer_wealth = 0
            for col in range(len(accounts[0])):
                customer_wealth += accounts[row][col]
            max_wealth=max(max_wealth,customer_wealth)
        return max_wealth