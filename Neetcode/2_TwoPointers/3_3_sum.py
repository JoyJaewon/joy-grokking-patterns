from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = [] 
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                num_sum = nums[i] + nums[left] + nums[right]

                if num_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
                # else라고 하면 틀림
                elif num_sum > 0:
                    right -= 1
                
                else:
                    left += 1
        
        return result

# TC: O(N^2), SC: O(1)