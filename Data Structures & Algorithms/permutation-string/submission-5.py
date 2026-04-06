class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        frq=[0]*256
        curfrq=[0]*256
        l=len(s1)
        for c in (s1):
            frq[ord(c)]+=1
        
        for i in range(len(s1)):
            curfrq[ord(s2[i])]+=1

        for i in range(len(s1),len(s2)):
            if frq==curfrq:
                return True
            else:
                curfrq[ord(s2[i-l])]-=1
                curfrq[ord(s2[i])]+=1
        return frq==curfrq        