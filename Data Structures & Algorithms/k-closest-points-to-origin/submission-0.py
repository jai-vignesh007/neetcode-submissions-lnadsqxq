class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for i in range(len(points)):
            d=math.sqrt((0-points[i][0])**2 +(0-points[i][1])**2)
            heapq.heappush(heap,(-d,i))
        while len(heap)!=k:
            heapq.heappop(heap)
        res = []
        while heap:
            d, i = heapq.heappop(heap)
            res.append(points[i])
        return res

        



        
        