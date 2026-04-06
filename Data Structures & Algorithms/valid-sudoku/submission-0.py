class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                row=f"{board[i][j]} in row {i}"
                col=f"{board[i][j]} in col {j}"
                box=f"{board[i][j]} in box {3*(i//3) + (j//3)}"
                if row in a or col in a or box in a:
                    return False
                a.append(row)
                a.append(col)
                a.append(box)
        return True
        