class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        
        #find leftmost
        
        def find_idx(start,end,target,flag):
            leftMostIndex = -1

            while start<=end:
                mid = start+(end-start)//2
                
                if target < nums[mid]:
                    end = mid-1
                elif target > nums[mid]:
                    start = mid+1
                else:
                    leftMostIndex = mid
                    if flag==0:
                        end = mid-1  #continue looking to the left
                    else:
                        start = mid+1 
                        
            return leftMostIndex
                    

        
        left = find_idx(0,len(nums)-1,target,0)
        right = find_idx(0,len(nums)-1,target,1)
        
        return [left,right]
        
                
                
                    
                    
                    
        
                
                
            
            
            
        
        
        
        
        
    
        
        
        