# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS Approach
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Cases
        if not p and not q:
            return True

        if not (p and q):
            return False

        if(q.val != p.val):
            return False

        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

        
        
        