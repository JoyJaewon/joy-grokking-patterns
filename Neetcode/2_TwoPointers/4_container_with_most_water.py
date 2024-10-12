from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            
            else:
                right -= 1
        
        return max_water

# TC: O(N), SC: O(1)