class Solution:
    
    def can_cut(self, ribbons: List[int], k: int, lenght:int) -> bool:
        cut = 0
        for ribbon in ribbons:
            cut+=ribbon//lenght
        return cut>=k

    def maxLength(self, ribbons: List[int], k: int) -> int:
        #pick a number from 1 to max(ribbons)->binary search
        #check if it all three can bit cut in that lenght (basically all are smaller or equial that that
        #keep looking
        start = 1
        end = max(ribbons)
        
        while start<=end:
            mid = start + (end-start)//2
            if self.can_cut(ribbons,k,mid):
                start = mid+1
            else:
                end = mid-1
            
        return end
            
            
            
            
        