class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0]*(n+1)
        g[0] = 1
        g[1] = 1
        
        for node in range(2,n+1):
            total = 0
            for root in range(1,node+1):
                left = root-1
                right = node - root
                total+= g[left]*g[right]
            g[node] = total
        return g[n]
        