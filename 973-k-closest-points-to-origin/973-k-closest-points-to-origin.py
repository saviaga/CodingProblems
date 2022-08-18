import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_eucledian(coord):
            x1,x2=coord            
            return math.sqrt((x1-0)**2+(x2-0)**2)
            
        distances = []
        
        for p in points:
            distances.append((get_eucledian(p),p))
        
        #print(distances)
        top_k = []
        for elem in distances:
            if len(top_k)<k:
                heapq.heappush(top_k, (elem[0]*(-1), elem[1]))
            else:
                heapq.heappush(top_k, (elem[0]*(-1), elem[1]))
                heapq.heappop(top_k)
            #print(top_k)
        
        return [elem[1] for elem in top_k]



        
  
            
   