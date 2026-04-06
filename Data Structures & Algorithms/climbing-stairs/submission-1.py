class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(i):
            if i >= n:
                if n==i:
                    return 1
                else:
                    return 0
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)