class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(start, end):
            #To get better performance on sorted or nearly sorted data we randomize 
            #by random sampling of one of the array elements as the pivot.
            #we swap the selected item with the last element
            
            ran = random.randint(start, end)
            pivot = end
            nums[pivot], nums[ran] = nums[ran], nums[pivot]
     
            # Index of smaller element
            border = start
            for cur in range(start, end):
                if nums[cur] >= nums[pivot]:
                    nums[cur], nums[border] = nums[border], nums[cur]
                    border += 1
            
            nums[border], nums[pivot] = nums[pivot], nums[border]
            return border

        def select(start, end, k_largest):
            """
            Returns the k-th smallest element of list within left..right
            """
            
            while start<=end:
                

                # get pivot index  
                pivot_index = partition(start,end)

                # the pivot is in its final sorted position
                if k_largest == pivot_index:
                     return nums[k_largest]
                # go left
                elif  pivot_index < k_largest:
                    start = pivot_index+1
                # go right
                else:
                    end = pivot_index-1

            # kth largest is (n - k)th smallest 
            return nums[k_largest]
        
        return select(0, len(nums)-1, k-1)
        
        