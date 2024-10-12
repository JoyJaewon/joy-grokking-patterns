class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            count_dict[s[right]] = count_dict.get(s[right], 0) + 1

            while (right - left + 1) - max(count_dict.values()) > k:
                count_dict[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        
        return longest

        