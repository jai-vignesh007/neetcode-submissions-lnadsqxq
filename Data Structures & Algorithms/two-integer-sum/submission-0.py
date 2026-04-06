class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,a in enumerate(nums):
            s=target-a
            if s in dic:
                return [dic[s],i]
            dic[a]=i   