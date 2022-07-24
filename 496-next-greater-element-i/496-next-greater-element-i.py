class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        dic_pairs = {}
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                dic_pairs[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        while stack:
            dic_pairs[stack.pop()] = -1
        print(dic_pairs)
        for i in range(len(nums1)):
            res.append(dic_pairs[nums1[i]])
            
        return res
        
                    
                    