class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        level=[]
        q=deque()
        q.append(root)
        while q:
            l=q.popleft()
            level.append(l.val)
            if l.right:
                q.append(l.right)
            if l.left:
                q.append(l.left)
        k-=1
        level.sort()
        return level[k]


        