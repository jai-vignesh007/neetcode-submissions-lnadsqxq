class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[0]*l
        for i in range(l):
            p=1
            for j in range(l):
                if i!=j:
                    p*=nums[j]
            res[i]=p
        return res
        
            



        

        
            

        