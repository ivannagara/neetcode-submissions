# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS method
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # In this problem; we are trying to see if the left height
        # and the right height difference is more than 1.
        # If its more than 1; then we return false;
        # and if its only 1 or 0; we return true.

        # We need to count this for every node.
        # If even one node is not balanced, then we will directly
        # return false.

        # If we want to use DFS; we then need to count the height of the current
        # to the bottom (left and right each).

        def getHeight(node: Optional[TreeNode]) -> int:
            # Base Case
            if not node:
                return 0
            
            leftHeight = getHeight(node.left)
            if (leftHeight == -1):
                return -1

            rightHeight = getHeight(node.right)
            if (rightHeight == -1):
                return -1

            diff = leftHeight - rightHeight
            if (abs(diff) > 1):
                return -1

            return (1 + max(leftHeight, rightHeight))

        return getHeight(root) != -1
            


        