class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        s=sorted(s1)
        print(s,s1)
        l2=len(s2)
        for i in range(len(s2)-l1+1):
            t=s2[i:i+l1]
            t=sorted(t)
            print(t)
            if t == s:
                return True
        return False

        
        
        


        