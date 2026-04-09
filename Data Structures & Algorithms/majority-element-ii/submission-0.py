class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=len(nums)
        majl=l//3
        arr={}
        ans=[]
        for i in nums:
            arr[i]=arr.get(i,0)+1
            if arr.get(i)>majl and i not in ans:
                ans.append(i)
        return ans

        









        