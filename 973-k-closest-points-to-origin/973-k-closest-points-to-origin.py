class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def get_eucledian(coord):
            x1,x2=coord
            
            return math.sqrt((x1-0)**2+(x2-0)**2)

        
        distances = []
        for p in points:
            distances.append([get_eucledian(p),p])
        
        distances.sort()
        
        return [elem[1] for elem in distances[:k]]
   
        
        
                             

            