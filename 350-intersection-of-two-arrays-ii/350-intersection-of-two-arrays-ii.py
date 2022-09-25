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
        
        #Approach2: Sort and Use Two pointers and check coincidences(do not care about duplicates)
        #sort arrays
        #Store in res
        #Time O(nlogn)
        #Space O(1) constant with variables + space of res
        
        nums1.sort()
        nums2.sort()
        
        idx1=0
        idx2=0
        res= []
        
        while idx1<len(nums1) and idx2<len(nums2):
            
            #move until they are equal
            if nums1[idx1] <nums2[idx2]:
                idx1+=1
                
            elif nums1[idx1] >nums2[idx2]:
                idx2+=1
               
            elif nums1[idx1]==nums2[idx2]:
                res.append(nums1[idx1])
                idx1+=1
                idx2+=1
        return res
            
            
                
                
                
                
        