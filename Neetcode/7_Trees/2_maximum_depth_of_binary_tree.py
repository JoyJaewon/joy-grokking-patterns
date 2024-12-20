from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        def dfs(node):
            if not node:
                return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))
        
        return dfs(root)
    
# BFS
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root)])
        level = 0

        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append((curr_node.left))
                if curr_node.right:
                    queue.append((curr_node.right))
            level += 1
        
        return level