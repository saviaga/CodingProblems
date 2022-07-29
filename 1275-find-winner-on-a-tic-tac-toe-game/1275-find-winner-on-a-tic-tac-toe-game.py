class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n=3
        lrows = [0]*n
        lcols = [0]*n
        diag = 0
        antidiag = 0
        remaining = n*n
        for i in range(len(moves)):
            remaining -=1
            current = moves[i]
            row = current[0]
            col = current[1]
            
            player = i%2
            

            points = 1  if player == 0 else -1
           
            #save score in rows and colums
            lrows[row] += points
            lcols[col] += points

            #save score in diagonal
            if row == col:
                diag+= points

            
            #save score in antidiagonal
            if row + col == n-1:  #antidiagona row+col alwaus sums to len(n)-1
                antidiag += points 

            #check if someone has won
            if points * n in (lrows + lcols+ [diag] + [antidiag]):
                return 'A' if points ==1 else 'B'
        if i+1 == n*n:
            return 'Draw'
        else:
            return "Pending"

            
        
        
        
        
        