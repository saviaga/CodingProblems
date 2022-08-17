class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        val = 0
        for elem in shift:
            direction,places = elem
            if direction==0:
                val+= -places
            else:
                val+= places
                
        rotation = val%len(s)
       
        res=''
        if rotation<0: #rotate to the left
            res= s[rotation:] + s[:rotation]  
        else: #rotate to the right
            res =  s[-rotation:] + s[:-rotation] 
            
        return res
       
     
            
        