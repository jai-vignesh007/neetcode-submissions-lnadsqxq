class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        l = 0
        for ch in s1:
            dic1[ch] = 1 + dic1.get(ch, 0)
        while l < len(s2) - len(s1) + 1:
            dic2 = {}
            for i in range(l, l+len(s1)):
                dic2[s2[i]] = 1 + dic2.get(s2[i], 0)

            l += 1
            if dic1 == dic2:
                return True

        return False