# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    @staticmethod
    def inorder(node):
        if not node:
            return []
        return BSTIterator.inorder(node.left) + [node.val] + BSTIterator.inorder(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.nodes = BSTIterator.inorder(root)
        
    def next(self) -> int:
        self.index+=1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        if self.index<len(self.nodes)-1:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()