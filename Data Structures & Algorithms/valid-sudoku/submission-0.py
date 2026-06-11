class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen1=set()#row
            seen2=set()#col
            seen3=set()#box
            for j in range(9):
                if (board[i][j]<"1"   or board[i][j]>"9" )and board[i][j]!=".":
                    return False
                if board[i][j]!="." :
                    if board[i][j] in seen1:
                        return False
                    else:
                        seen1.add(board[i][j])
                if board[j][i]!=".":
                    if board[j][i] in seen2:
                        return False
                    else:
                        seen2.add(board[j][i])
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = set()

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        if board[i][j] != ".":

                            if board[i][j] in seen:
                                return False

                            seen.add(board[i][j])

        return True