class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        mapping =set(jewels)
        count = 0
        for elem in stones:
            if elem in mapping:
                count+=1
        return count
                
        