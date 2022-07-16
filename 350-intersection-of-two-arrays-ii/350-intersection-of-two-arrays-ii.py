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
            dic_nums1 = Counter(nums1)
            for elem in nums2:
                if elem in dic_nums1:
                    dic_nums1[elem] -=1
                    res.append(elem)
                    if dic_nums1[elem]==0:
                        del dic_nums1[elem]
            return res

                
                
        