# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS method
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # This is the base case for the recursion
    #     if not root:
    #         return None
    
    #     # In each node; lets swap the left and right
    #     root.left, root.right = root.right, root.left

    #     self.invertTree(root.left)
    #     self.invertTree(root.right)

    #     return root

    # BFS method
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # Check if root is valid
    #     if not root:
    #         return None
        
    #     # initialize the queue with the root inside it
    #     q = deque([root])
    #     while q:
    #         # We get the first in line node
    #         node = q.popleft()
    #         # Then we swap its children to the invert version
    #         node.left, node.right = node.right, node.left
    #         # Then we prepare the next queue for the next while loop
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     return root

    # DFS method
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
        
    #     # The DFS will directly loop to the bottom-most of the node first
    #     root.left, root.right = root.right, root.left
    #     self.invertTree(root.right)
    #     self.invertTree(root.left)

    #     return root

    # BFS method
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # We will initialize queue here so that we can traverse through the nodes
        # from up to the bottom
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                # We first swap the current layer first
                node.right, node.left = node.left, node.right
                # after we swap; we then append the child of current layers
                if(node.right):
                    q.append(node.right)
                if(node.left):
                    q.append(node.left)

        return root

            
            



        