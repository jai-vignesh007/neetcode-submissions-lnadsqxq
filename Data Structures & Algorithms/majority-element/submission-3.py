class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=nums[0]
        c=0
        for i in nums:
            if i==el:
                c+=1
            else:
                c-=1
            if c<=0:
                el=i
        return el
        