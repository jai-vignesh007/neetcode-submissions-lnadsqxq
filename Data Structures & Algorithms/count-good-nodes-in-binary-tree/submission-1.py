# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q=deque()
        q.append((root,-float('inf')))
        counter=0
        while q:
              
            node,max_sofar=q.popleft()
            if node.val >= max_sofar:
                counter+=1
                max_sofar=node.val

            if node.left:
                q.append((node.left,max_sofar))
            if node.right:
                q.append((node.right,max_sofar))
        return counter 
        