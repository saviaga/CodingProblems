class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_eucledian(coord):
            x1,x2=coord
            
            return math.sqrt((x1-0)**2+(x2-0)**2)

       
        distances = []
        for p in points:
            heapq.heappush(distances,(get_eucledian(p),p))
        
   
        return [heapq.heappop(distances)[1]  for _ in range(k)]
  
            
   