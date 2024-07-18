# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        head = TreeNode()
        curr = head
        stack = [root]
        
        while stack:
            node = stack.pop()
            curr.right = TreeNode(node.val)
            curr = curr.right
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        root.right = head.right.right
        root.left = None
            
        