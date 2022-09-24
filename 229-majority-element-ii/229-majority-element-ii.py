class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #[3,2,3]  -> 2
        #[1] -> 
        #[1,2] -> [1,2]
        
        #approach 1:  hashmap
        # got throught each element store in hashmap(eg.3:2)
        #got throgh the hashmap and check if value >n/3 if yes then add to the resulting list
        #Time O(N)
        #Space O(N) depends on the # of different elems in nums
        #approach 2: Boyer-Moore:
        #keep two counters and two candidates
        #2 potential numbers can be > n/3
        #only if next element is != than current candidates 
        #decrease the counters
         
        
        candidate1=None
        candidate2=None
        counter1=0
        counter2=0
        result = []
        for elem in nums:
            if elem==candidate1:
                counter1+=1
            elif elem==candidate2:
                counter2+=1
            elif counter1==0:
                candidate1=elem
                counter1+=1
            elif counter2==0:
                candidate2=elem
                counter2+=1
            else:
                counter1-=1
                counter2-=1
                
        if nums.count(candidate1)>len(nums)//3:
            result.append(candidate1)
        if nums.count(candidate2)>len(nums)//3:
            result.append(candidate2)
        return result
            
                
            