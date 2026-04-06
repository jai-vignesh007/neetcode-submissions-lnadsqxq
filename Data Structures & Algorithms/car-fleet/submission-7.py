class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack=[]
        stack.append(-1)
        c=0
        for p,s in pair:
            t=(target-p)/s
            if t > stack[-1]:
                stack.pop()
                stack.append(t)
                c+=1
        return c                      