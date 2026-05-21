# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, rootA: Optional[Node], rootB: Optional[Node]) -> bool:
        if not rootA and not rootB:
            return True
        if not rootA or not rootB:
            return False
        if rootA.val != rootB.val:
            return False
        return self.isSameTree(rootA.left, rootB.left) and self.isSameTree(rootA.right, rootB.right)