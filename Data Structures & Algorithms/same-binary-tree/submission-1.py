# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return True
            
            if not q:
                return False

            if not p:
                return False

            print("p.val : ", p.val, "q.val : ", q.val)
            if p.val == q.val and p and q:
                # print("Inside False")
                # return False

                return dfs(p.left, q.left) and dfs(p.right, q.right)

            return False


        

        return dfs(p,q)
        



        