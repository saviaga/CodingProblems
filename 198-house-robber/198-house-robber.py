class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        #[rob1,rob2,n,n+1..]
    
        rob1, rob2 = 0, 0
        for n in nums:
        
            temp = max(n + rob1, rob2) #imagine we are in n position, we have two choices
            rob1 = rob2 #iterate n+1 we want to update rob1 to advance to rob2
            rob2 = temp #the choice we made in n
        return rob2
   
    
    
        
     