from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                target = num + 1
                cnt = 1

                while target in num_set:
                    target += 1
                    cnt += 1
                
                longest = max(longest, cnt)
        
        return longest
        