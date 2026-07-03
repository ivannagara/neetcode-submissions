# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS Approach
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        # We need to traverse the tree
        # from the top to bottom wards;

        # This function, we need to make it recursive
        # So it keeps on going down and checking the nodes
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True

        if (not p and q) or (p and not q) or (q.val != p.val):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
            

