class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_eucledian(coord):
            x1,x2=coord
            
            return math.sqrt((x1-0)**2+(x2-0)**2)

       
        distances = []
        for p in points:
            distances.append((get_eucledian(p),p))
        heapq.heapify(distances)
        
   
        return [heapq.heappop(distances)[1]  for _ in range(k)]

        #time: O(N + KlogN) -> N to get the distances, and KlogN for the heap (each pop is logN and there are K elements)
    
        #space O(N)
  
            
   