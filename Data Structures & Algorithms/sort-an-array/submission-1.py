class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result=[]
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        right=nums[mid:]
        left=nums[:mid]
        left=self.sortArray(left)
        right=self.sortArray(right)
        i=0
        j=0
        while i<len(left) and j< len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result+=left[i:]
        result+=right[j:]
        return result    