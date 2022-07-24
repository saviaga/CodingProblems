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
                prices[stack.pop()]-=pr
            stack.append(i)
            
        return prices
                
        