class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        idx_new = len(nums1)-1
        m = m -1
        n = n -1
        
        while m >= 0 and n>=0:
            if nums1[m] >= nums2[n]:
                nums1[idx_new] = nums1[m]
                m-=1
            else:
                nums1[idx_new] = nums2[n]
                n-=1
            idx_new-=1
        
        while m>=0:
            nums1[idx_new] = nums1[m]
            m-=1
            idx_new-=1
        while n>=0:
            nums1[idx_new] = nums2[n]
            n-=1
            idx_new-=1
        return n
            
                
        
        
        
        
        
        