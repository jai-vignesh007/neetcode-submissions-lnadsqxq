class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        
        for i in range(len(numbers)):
            l,r=i+1,length-1
            val=target-numbers[i]
            while l<=r:
                m=(l+r)//2
                if numbers[m] < val:
                    l=m+1
                elif numbers[m] > val:
                    r=m-1
                else:
                    return [i+1,m+1]
        return []


        