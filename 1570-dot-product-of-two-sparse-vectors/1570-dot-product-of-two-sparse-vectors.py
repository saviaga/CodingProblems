class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        #get the index and values of non-zeros
        self.nonzeros = []
        for i,v in enumerate(nums):
            if v!=0:
                self.nonzeros.append((i,v))
                
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        i=0
        j=0
        dot_product=0
        while i < len(self.nonzeros) and j<len(vec.nonzeros):
            i_idx, i_num = self.nonzeros[i]
            j_idx, j_num = vec.nonzeros[j]
            
            if i_idx==j_idx:
                dot_product+= i_num*j_num
                i+=1
                j+=1
            elif i_idx>j_idx:
                j+=1
            else:
                i+=1
        return dot_product
            
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)