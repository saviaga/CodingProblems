class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        k=k-1
        def quickselect(l,r,nums):
            #
            
            pivot = nums[r]
            p = l
            for i in range(l,r):
                
                if nums[i][1] > pivot[1]:
                    nums[p], nums[i] = nums[i],nums[p]
                    p+=1
            nums[p],nums[r]= nums[r],nums[p]
            if p > k: return quickselect(l,p-1,nums)
            elif p < k: return quickselect(p+1,r,nums)
            else:   
                return [elem[0] for elem in nums[:k+1]]
        
        items = {}
        for elem in nums:
            items[elem] = items.setdefault(elem,0)+1
        
            
        
        return quickselect(0,len(items)-1,list(items.items()))
        