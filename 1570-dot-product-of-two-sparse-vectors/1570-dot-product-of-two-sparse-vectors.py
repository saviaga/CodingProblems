class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros=[]
        for index,value in enumerate(nums):
            if value!=0:
                self.nonzeros.append((index,value))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i=0
        j=0
        while i < len(self.nonzeros) and j<len(vec.nonzeros):
            idx_i,valuei = self.nonzeros[i]
            idx_j,valuej = vec.nonzeros[j]
            if idx_i==idx_j:
           
                result+= valuei* valuej
                i+=1
                j+=1
            elif idx_i>idx_j:
                j+=1
            elif idx_i<idx_j:
                i+=1
        return result
        
 #The “nums” part is an attribute on the SparseVector class. The question passes you another SparseVector class to do the dot product with. So self.nums refers to the current SparseVector and it’s numbers and the vec.nums refers to the other sparse vector class.       
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)