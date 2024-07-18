# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaves(node):
            if not node:
                return

            if not (node.left or node.right):
                yield node.val

            yield from get_leaves(node.left)
            yield from get_leaves(node.right)

        return [*get_leaves(root1)] == [*get_leaves(root2)]
