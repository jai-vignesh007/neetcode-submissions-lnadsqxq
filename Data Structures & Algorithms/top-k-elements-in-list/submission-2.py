class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for _ in range(len(nums)+1) ]

        for num in nums:
            count[num]=1+count.get(num,0)
        
        for num,key in count.items():
            freq[key].append(num)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res)==k:
                    return res
                            

        
        




        