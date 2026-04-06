class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                p=prices[j]-prices[i]
                mp=max(p,mp)
        return mp