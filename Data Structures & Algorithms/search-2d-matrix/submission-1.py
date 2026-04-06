class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # find first row whose last element >= target
        tr = None
        for i in range(m):
            if matrix[i][n - 1] >= target:
                tr = i
                break

        if tr is None:          # target is larger than every row's last element
            return False

        # scan that row
        for j in range(n):
            if matrix[tr][j] == target:
                return True
        return False
