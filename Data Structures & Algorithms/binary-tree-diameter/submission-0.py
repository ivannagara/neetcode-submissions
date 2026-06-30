# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS method
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initially; we should set the base case
        if not root:
            return 0

        maxHeight = 1
        # To get this answer; this essentially means that we are trying to
        # find the maximum value of =>
        # height of "left sub-tree" + "right sub-tree"
        # So, we need to keep on adding the height from each of a successful
        # recursive function
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        