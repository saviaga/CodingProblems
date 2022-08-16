class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #get the index and values of non-zeros
        self.nonzeros = {}
        for i,v in enumerate(nums):
            if v!=0:
                self.nonzeros[i] = v
                
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        result=0
        for k,v in self.nonzeros.items():
            if k in vec.nonzeros:
                result+= v*vec.nonzeros[k]
        return result
            
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)