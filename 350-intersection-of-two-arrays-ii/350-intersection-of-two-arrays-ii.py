class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #Approach 1:
        #store nums1 in a map and count ocurrences
        #loop trhough nums2 and check if is in map and ocurrences>0:
        #if yes, store in res and rest ocurrences
        #Time O(N+M), we need to loop through both arrays
        #Space O(m) number of distinct characters in nums1 + space of res
        
        #Approach2: Use Two pointers and check coincidences(do not care about duplicates)
        #sort arrays
        #Store in res
        #Time O(nlogn)
        #Space O(1) constant with variables + space of res
        
        mapping = Counter(nums1)
        res = []
        for elem in nums2:
            if elem in mapping and mapping[elem]>0:
                res.append(elem)
                mapping[elem]-=1
        return res
                
                
                
        