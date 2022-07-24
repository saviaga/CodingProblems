class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        dic_pairs = {}
        stack = []
        for i,pr in enumerate(prices):
            #print(stack)
            while stack and pr <= prices[stack[-1]]:
                original_p = stack.pop()
                prices[original_p]-=pr
            stack.append(i)
            
        return prices
                
        