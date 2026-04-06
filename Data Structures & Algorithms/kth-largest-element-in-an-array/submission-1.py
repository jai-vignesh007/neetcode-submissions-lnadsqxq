class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p=[]
        for i in range(len(nums)):
            heapq.heappush(p,nums[i])
            if len(p)>k:
                heapq.heappop(p)
        return p[0]
        
        