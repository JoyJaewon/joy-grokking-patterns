# version 1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = {}, {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            s2_count[s2[left]] -= 1
            # 값이 0인 경우 해당 키 삭제 (비교를 위해 필요)
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]] 
                
            if s1_count == s2_count:
                return True
            left += 1
        
        return False

# version 2 - defaultdict
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        
        if s1_count == s2_count:
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] += 1
            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
            
            if s1_count == s2_count:
                return True
            
            left += 1
        
        return False

# version 3 - list
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0] * 26
        count_s2 = [0] * 26 

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
                
        if count_s1 == count_s2:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            count_s2[ord(s2[right]) - ord('a')] += 1
            count_s2[ord(s2[left]) - ord('a')] -= 1
            if count_s1 == count_s2:
                return True
            left += 1
        
        return False
        

        