class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic_pairs = {}
        stack = []
        res = []
        for elem in nums2:
            while stack and elem > stack[-1]:
                dic_pairs[stack.pop()]=elem 
            stack.append(elem)
            
        while stack:
            dic_pairs[stack.pop()]=-1
        
        for elem in nums1:
            res.append(dic_pairs[elem])
            
        return res
    
    
    