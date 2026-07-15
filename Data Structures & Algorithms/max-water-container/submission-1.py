class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1

        max_water = min(heights[i], heights[j]) * (j-i)

        while i < j:
            current_water = min(heights[i], heights[j]) * (j-i)
            if current_water > max_water:
                max_water = current_water
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
        
        return max_water
        