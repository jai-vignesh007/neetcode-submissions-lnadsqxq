# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            # print('qLen : ', qLen)
            # print('q : ', q)
            for i in range(qLen):
                node = q.popleft()
                # print("inside q : ", q)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)
        
        return res

