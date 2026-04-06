class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxcontent=0
        while l < r:
            # m=(l+r)//2
            if heights[l]<=heights[r]:
                small=heights[l]
                content= small * (r-l)
                l+=1
            elif heights[l]>heights[r]:
                small=heights[r]
                content= small * (r-l)
                r-=1
            if content > maxcontent:
                maxcontent=content
        return maxcontent
             
        

