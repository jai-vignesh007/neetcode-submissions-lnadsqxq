# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1=[]
        tree2=[]
        def dfs1(root):
            if not root:
                tree1.append(None)
                return 
            dfs1(root.left)
            # print()
            # tree1.append(root.val)
            dfs1(root.right)
            tree1.append(root.val)
        
      
        def dfs2(root):
            if not root:
                tree2.append(None)
                return 
            dfs2(root.left)
            # print()
            # tree2.append(root.val)
            dfs2(root.right)
            tree2.append(root.val)
        
        dfs1(p)
        dfs2(q)
        print(tree1)
        print(tree2)


        return tree1==tree2
        



        