# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(node=root, sum=0):
            nonlocal res

                
               
            
            if node.left:
                dfs(node.left, sum*10+node.val)
            if node.right:
                dfs(node.right, sum*10+node.val)
            if not (node.left or node.right):
                res += sum*10+node.val
                
            
        dfs()
        
        return res
        