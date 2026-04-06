class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        ans=0
        maxi=max(piles)
        while mini<=maxi:
            k=math.ceil((maxi+mini)/2)
            th=0
            for p in piles:
                th+=math.ceil((p/k))
            if th <= h:
                ans=k
                maxi=k-1
            else:
                mini=k+1
        return ans





        


    
        