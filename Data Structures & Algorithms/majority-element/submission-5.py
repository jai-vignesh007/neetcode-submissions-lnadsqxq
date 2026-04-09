class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = 0
        c = 0
        
        for i in nums:
            # 1. If counter is 0, pick a new candidate first
            if c == 0:
                el = i
            
            # 2. Then update the counter based on that candidate
            if i == el:
                c += 1
            else:
                c -= 1
                
        return el