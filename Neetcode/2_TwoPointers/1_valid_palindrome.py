# TC: O(N), SC: O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_char = [c.lower() for c in s if c.isalnum()]

        left, right = 0, len(filtered_char) - 1

        while left < right:
            if filtered_char[left] != filtered_char[right]:
                return False
                
            left += 1
            right -= 1
        
        return True


# TC: O(N), SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
        
