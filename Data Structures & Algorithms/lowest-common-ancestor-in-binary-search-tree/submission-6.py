# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (not root) or (not p) or (not q):
            return None

        # Lets start at the top of the tree
        current = root

        # Lets loop it
        # Because this is Binary Search Tree (BST); we know the lower numbers is on the
        # left node, and bigger ones is on the right node
        while current:
            # So we first check if the defined 'p' and 'q' is larger than our current node;
            # we move to the "right" node because we want to approach that value
            
            # Rule 1: if both targets bigger than the current node; lets move right
            if (p.val > current.val) and (q.val > current.val):
                current = current.right

            # Rule 2: if both targets are lower than the current node value, lets move left
            if (p.val < current.val) and (q.val < current.val):
                current = current.left
            
            # Rule 3: They split up or we hit one; this is our closest Lowest Common Ancestor
            else:
                return current
        
        return None

