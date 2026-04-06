class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        
        heap=[]
        res=[]
        for v,ke in count.items():
            heapq.heappush(heap,(ke,v))
            if len(heap)>k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res       