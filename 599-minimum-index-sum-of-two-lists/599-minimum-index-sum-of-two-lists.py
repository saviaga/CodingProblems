class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        #Approach 1: nested loops
        #grab elem list1 find in elem 2: store tuple(word,sum_index)
        #go thought the set and return the lowests (2 if there are coincidences)
        #store in a result list
        
        #Time O(N^2)
        #space: set-> O(N) worst case if both lists are same size and all elem coincide
        
        #Approach 2:(
        #store first one in hasmap (word,index)
        #go througnt the second one and if there is coincidence , then update map with new sum_index
        #check if the sum is lowest so far, if it is 
        #return the two lowest:
        #Time O(l1+l2)
        #Space O(m) worst case all elements coincide
        
        mapping = {}
       
        for i in range(len(list1)):
            elem = list1[i]       
            mapping[elem]=i
           
        
        min_sum = float('inf')
        for i in range(len(list2)):
            elem = list2[i]
            if elem in mapping: 
                curr_sum = mapping[elem]+i
                if curr_sum > min_sum:
                    break
                if curr_sum < min_sum:
                    res = [elem]
                    min_sum = curr_sum
                elif curr_sum == min_sum:
                        res.append(elem)
        return res
                
        
        
        
        