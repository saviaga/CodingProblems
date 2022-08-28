class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
 
        def find_idx(left,right,search_left):
            i=-1
            while left  <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid -1 
                else:
                    i=mid
                    if search_left: 
                        right = mid-1
                    else:
                        left = mid + 1
            return i

        
        left = 0
        right= len(nums) - 1
        leftelem = find_idx(left,right,1)
        rightelem = find_idx(left,right,0)
        return [leftelem,rightelem] 
       
                             
                                
                
                    
                    
                    
        
                
                
            
            
            
        
        
        
        
        
    
        
        
        