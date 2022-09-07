class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #[-4,-1,1,2]
        
        closest = float('inf')
        nums.sort()

        count = 0
        for i in range(len(nums)-2):
            
            s= i+1
            e= len(nums)-1
            
            while s<e:
          
                suma = nums[i] + nums[s] + nums[e]
                if abs(target-suma) < abs(closest):
                    closest = target - suma 
             
                if suma < target:                   
                    s+=1
                else:                   
                    e-=1
                if closest == 0:
                    break
        return target - closest
        
        

                    
        