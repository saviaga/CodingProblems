class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        
        #find leftmost
        
        def find_left(left,right,target):
            
            while left  < right:
                mid = (left + right) // 2
                if target > nums[mid]:
                   
                    left = mid + 1
                else:
                    right = mid 
           
            return left
        def find_right(left,right,target):
            i=-1
            while left  <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid -1
                else:
                    i=mid
                    left = mid+1
            return i

        
        left = 0
        right= len(nums) - 1
        leftelem,rightelem = -1,-1
        leftelem = find_left(left,right,target)
        rightelem = find_right(left,right,target)
        #print(leftelem,rightelem)
        if nums[leftelem]==target and  nums[rightelem]==target:
            return [leftelem,rightelem] 
        else:
            return [-1,-1]
                             
                                
                
                    
                    
                    
        
                
                
            
            
            
        
        
        
        
        
    
        
        
        