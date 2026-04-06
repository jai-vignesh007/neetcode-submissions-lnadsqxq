class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Task_Frequecy=Counter(tasks)
        maxHeap=[-val for val in Task_Frequecy.values()]
        time=0
        q=deque()
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time+=1
            if maxHeap:
                taskfrq=1+heapq.heappop(maxHeap)
                if taskfrq:
                    q.append([taskfrq,time+n])
            if q and q[0][1]==time:
                val=q.popleft()
                heapq.heappush(maxHeap,val[0])
        return time
            
        