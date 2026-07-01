# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS method - Brute Force
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     maxLength = 1

    #     # Diameter means the longest length from one edge to another one
    #     # this means we need to find in one node; which one is the
    #     # longest left + longest right length sum.

    #     # First; we want to use a recursive function that gets the max
    #     # height from the current node; so lets make this function [getMaxLength]

    #     # Then, lets recurse this function to keep on getting the biggest diameter
    #     leftHeight = self.getMaxLength(root.left)
    #     rightHeight = self.getMaxLength(root.right)
    #     diameter = leftHeight + rightHeight
    #     sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    #     return max(diameter, sub)

    # def getMaxLength(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     return (1 + max(self.getMaxLength(root.left), self.getMaxLength(root.right)))


    # DFS
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     maxHeight = 0
    #     # Diameter is current node's left depth + right depth
    #     # Then; we can just get the max of our current biggest diameter
    #     # vs the contender diameter

    #     # Get left and right depths of the current node (using the DFS recursion)
    #     def getHeight(root: Optional[TreeNode]) -> int:
    #         nonlocal maxHeight

    #         if not root:
    #             return 0
    #         left = getHeight(root.left)
    #         right = getHeight(root.right)
    #         height = left + right

    #         # get the current node's height before the values disappear
    #         maxHeight = max(maxHeight, height)

    #         # Just return the current max height of this current node
    #         return 1 + max(left, right)

    #     getHeight(root)
    #     return maxHeight

    # DFS
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDiameter = 0

        # The diameter is the length of left node height + right node height

        # First; we want to recursively get the height of the current node of the
        # tree

        # This recursion is the recursion that gets to the bottom of the tree,
        # and in each node, this will get executed. So, in this formula,
        # we need to get the current diameter of the tree here.
        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            nonlocal maxDiameter
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)
            diameter = leftHeight + rightHeight
            # Here in every node, we compare if the current diameter is bigger than the recorded max
            # diameter
            maxDiameter = max(maxDiameter, diameter)

            # Its the same as the regular getting tree height DFS method formula =>
            return(1 + max(leftHeight, rightHeight))

        getHeight(root)
        return maxDiameter



        