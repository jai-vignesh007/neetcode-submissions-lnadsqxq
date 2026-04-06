class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[0]*l
        zc,p=0,1
        for num in nums:
            if num:
                p*=num
            else:
                zc+=1
        if zc>1:
            return res
        if zc:
            for i in range(l):
                if nums[i]==0:
                    res[i]=p
                else:
                    res[i]=0 
            return res
        for i,a in enumerate(nums):
            res[i]=p//a
        return res



        
        
            



        

        
            

        