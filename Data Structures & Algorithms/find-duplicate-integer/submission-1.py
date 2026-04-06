class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=len(nums)
        arr=[-1]*l
        for n in nums:
            if arr[n]!=-1:
                return n
            arr[n]=n