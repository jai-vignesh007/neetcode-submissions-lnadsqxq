class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=len(nums)
        qulilen=l//3
        ans=set()
        arr={}
        for i in nums:
            arr[i]=arr.get(i,0)+1
            if arr[i] > qulilen:
                ans.add(i)
        return list(ans)

        









        