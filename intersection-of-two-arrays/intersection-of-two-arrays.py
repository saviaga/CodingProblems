class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        #Output [4,9]
        
        #Input: nums1 = [], nums2 = [9,4,9,8,4]
        #Output: []
        
        #nums1 = [], nums2 = []
        #Output: []
        
        #Input: nums1 = [1,1,2,2], nums2 = [2,2]
        #Output: [2,2]
       
        #Approach 1:
        # go throught the array1 and check if number in array2
            #if True:  store in result (set)
        #Return set as list
        #Time O(mxn)
        #Space O(1) -> if we do not count the resulting array
        
        #Approach 2:
        #two sets
        #1. convert nums1 to set
        #2. convert mums2 to set
        #4. check if elements in set1 are in set2
        
        #Time complexity: O(n+m)
        #Space complexity O(n+m)
        
        #Approach 3: 
        #********Assuming both are sorted******* 
        #Use two pointers to compare the coincidences
        #store coincidences in new array
        #Time Complexity: 0(n+m) O(n) time is used to convert nums1 into set, \mathcal{O}(m)O(m) time is used to convert nums2, and contains/in operations are \mathcal{O}(1)O(1) in the average case.
        #Space complexity O(m+n) in the worst case when all elements in the arrays are different.  #not considerin the resulting array
        
        nums1.sort()
        nums2.sort()
        
       
        left = 0
        right = 0
        result = []
        while left<len(nums1) and right<len(nums2):
         
            if left!=0 and  nums1[left] == nums1[left-1]: #deal with duplicates
                    left+=1
                    continue
            
            if nums1[left]== nums2[right]:
                result.append(nums1[left])
                left+=1
                right+=1
                
            elif nums1[left] < nums2[right]:
                left+=1
            elif nums1[left] > nums2[right]:
                right+=1
            
        return result
                
                
        
        
        
        