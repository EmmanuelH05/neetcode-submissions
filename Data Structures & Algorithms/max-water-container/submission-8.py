class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0

        L, R = 0, len(heights) - 1 
        
        maxArea = 0

        while L < R:
            curArea = (R - L) * min(heights[L], heights[R])
            maxArea = max(maxArea, curArea)

            if heights[L] < heights[R]:
                L += 1 
            else:
                R -= 1
        return maxArea

