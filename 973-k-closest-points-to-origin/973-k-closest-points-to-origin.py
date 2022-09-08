import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

      
            
       
        k=k-1
        def quickselect(l,r):
            random = randint(l,r)
            points[random], points[r] = points[r], points[random]
            pivot = points[r]
  
            p = l
            for i in range(l,r):
                
                if  (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                    points[p], points[i] = points[i],points[p]
                    p+=1
            points[p],points[r]= points[r],points[p]
          
            if p > k: return quickselect(l,p-1)
            elif p < k: return quickselect(p+1,r)
            else:   return points[:k+1]
            
        return quickselect(0,len(points)-1)

    
        




        
  
            
   