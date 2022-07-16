class Solution(object):
        
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        else:
            res = []
            p1 = 0
            p2 = 0
            nums1.sort()
            nums2.sort()
            while p1<len(nums1) and p2 < len(nums2):
                
                if nums1[p1] < nums2[p2]:
                    p1+=1
                elif nums1[p1] > nums2[p2]:
                    p2+=1
                elif nums1[p1] == nums2[p2]:
                   
                    res.append(nums1[p1])
                    p2+=1
                    p1+=1
            return res

                
                
        