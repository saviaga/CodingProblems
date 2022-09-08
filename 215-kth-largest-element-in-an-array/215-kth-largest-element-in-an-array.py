class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums)-k
        
        def quickselect(l,r):
            
            pivot = nums[r]
  
            p = l
            for i in range(l,r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r]= nums[r],nums[p]
            if p > k: return quickselect(l,p-1)
            elif p < k: return quickselect(p+1,r)
            else:   return nums[p]
            
        return quickselect(0,len(nums)-1)
        
                
        
        
        