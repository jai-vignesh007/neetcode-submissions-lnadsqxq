class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers=set(nums)
        largest=0
        for n in nums:
            if n in numbers:
                l=1
            while n+1 in numbers:
                l+=1
                n+=1
            largest=max(l,largest)
        return largest


        
