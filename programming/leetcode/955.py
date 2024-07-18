# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque()
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            self.queue.append(node)
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
    def insert(self, val: int) -> int:       
        node = self.queue[0]
        
        if node.left is None:      
            node.left = TreeNode(val)
            self.queue.append(node.left)
            return node.val
        
        if node.right is None:
            node.right = TreeNode(val)
            self.queue.append(node.right)
            return node.val
        
        self.queue.popleft()
        return self.insert(val)

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()