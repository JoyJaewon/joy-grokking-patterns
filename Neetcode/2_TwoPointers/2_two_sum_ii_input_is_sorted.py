from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []

        while left < right:
            num_sum = numbers[left] + numbers[right]

            if num_sum == target:
                return [left + 1, right + 1]

            if num_sum > target:
                right -= 1
            
            else: 
                left += 1
        
        return [-1, -1]

# TC: O(N), SC: O(1)