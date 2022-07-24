class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        #Rules
        #0-0 , 1-1,6-9,8-8,9-6
        #2,3,4,5,7
        
        num_rot = []
        
        
        for i in range(len(num)-1,-1,-1):
            if num[i] in ['2','3','4','5','7']:
                return False
            elif num[i]=='6':
                num_rot.append('9')
            elif num[i]=='9':
                num_rot.append('6')
            else:
                num_rot.append(num[i])               
        
        num_rot =  "".join(num_rot)
        
        print(num_rot)
        return num_rot==num
                
                
        
        