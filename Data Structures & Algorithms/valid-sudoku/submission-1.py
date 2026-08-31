class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        small_grid = defaultdict(set)
        line_grid = defaultdict(set)
        col_grid = defaultdict(set)

        for line in range(len(board)) :
            
            

            for col in range(len(board[0])) : 

                if board[line][col] != "." :

                    # line 
                    if board[line][col] in line_grid[line] : 
                        return False 
                    else :
                        line_grid[line].add(board[line][col])


                    # col 
                    if board[line][col] in col_grid[col] : 
                        return False 
                    else :
                        col_grid[col].add(board[line][col])

                    # 3x3 grid 

                    if board[line][col] in small_grid[(col//3,line//3)] : 
                        return False 
                    else :
                        small_grid[(col//3,line//3)].add(board[line][col])
        return True 






        