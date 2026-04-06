class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # print(cost)
        l = [0] * (len(cost))
        l[0], l[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            l[i] = min((l[i-1] + cost[i]), (l[i-2] + cost[i]))
        # print(l)
        return l[-1]
