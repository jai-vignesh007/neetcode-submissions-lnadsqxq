class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag=[True]
        def dfs(root,cd):
            if not root:
                return cd-1
            l=dfs(root.left,cd+1)
            r=dfs(root.right,cd+1)
            if abs(l-r)>1:
                flag[0]=False
            return max(l,r)

        dfs(root,1)
        return flag[0]