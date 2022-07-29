class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.row= [0] * n
        self.col= [0] * n
        self.diag=0
        self.antidiag=0 
        
    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        points = 1 if player == 1 else -1
          
        
        
        self.row[row] += points
        self.col[col] += points
        if row == col:
            self.diag += points
        if row + col == self.n - 1:
            self.antidiag += points
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag)==self.n or abs(self.antidiag)==self.n:
            return player
        
        return 0
    
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)