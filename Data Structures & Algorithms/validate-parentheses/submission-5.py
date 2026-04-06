class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            "}":"{",
            "]":"[",
            ")":"("
        }
        
        stack=[]
        ob="{[("
        cb="}])"
        if s[0] in cb or len(s)%2!=0:
            return False
        for i in s:
            if i in ob:
                stack.append(i)
            else:
                if stack and stack[-1]==dic[i]:
                    stack.pop()
                else: return False
        
        return True if not stack else False 








                        