class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row validator
        for item in board:
            item = [char for char in item if char != "."]
            if len(set(item)) != len(item):
                return False
        
        #Column Validator
        column_checker = []
        i = 0
        for j in range(9):
         for item in board:
            if item[j] == ".":
                continue
            else:
                column_checker.append(item[j])
         if (len(set(column_checker))) != len(column_checker):
            return False
         column_checker = []

        # Square checker
        square = []
        x_starting = 0
        y_starting = 0
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    if board[x_starting + j][y_starting + k] == ".":
                        continue
                    else: 
                        square.append(board[x_starting + j][y_starting + k])
            if len(set(square)) != len(square):
                return False
            if x_starting < 6:
                x_starting += 3
            else:
                x_starting = 0
                y_starting += 3
            square = []

        return True



            


        