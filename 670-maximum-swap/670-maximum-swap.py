class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        #save the largest
        max_so_far = num
        

        lstnum = [int(i) for i in str(num)]

        #store indexes in dic
        
       
        
        for i in range(len(lstnum)-1): #we do not check the last nubmer is our need to swap
            max_num = max(lstnum[i+1:])
            
            if max_num > lstnum[i]:
                    
                    for j in range(len(lstnum)-1, i, -1): #find the index of the max num starting from left
                        if lstnum[j] == max_num:
                            break
                    lstnum[i],lstnum[j] = lstnum[j],lstnum[i]
                    break
                                    
        return "".join([str(i) for i in lstnum])
        
            
        
            
        
        