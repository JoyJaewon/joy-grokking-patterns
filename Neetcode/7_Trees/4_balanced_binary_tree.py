from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isBalanced = True
        
        def dfs(node):
            nonlocal isBalanced
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                isBalanced = False

            return 1 + max(left, right)
        
        dfs(root)
        return isBalanced
        