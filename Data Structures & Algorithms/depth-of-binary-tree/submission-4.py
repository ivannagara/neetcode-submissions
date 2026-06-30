# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS - Recursion Approach
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

    # BFS Approach
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     #Lets check if the root is null or not
    #     if not root:
    #         return 0

    #     q = deque()
    #     q.append(root)

    #     # We initialize this counter of depth
    #     depth = 0
    #     # We also want to keep on removing layer-by-layer so that
    #     # we can get the height of the Binary Tree
    #     while q:
    #         # We loop througout the same layer first
    #         for i in range(len(q)):
    #             # We GET the value and directly pop the first variable on the queue
    #             node = q.popleft()
    #             # If LEFT child node exists; we append it to queue
    #             if node.left:
    #                 q.append(node.left)
    #             # If RIGHT child node exists; we append it to queue
    #             if node.right:
    #                 q.append(node.right)
    #         # After we are done looping one layer and changed it to the
    #         # next layer's queue value; we then increment the `depth` by 1
    #         depth += 1
        
    #     return depth


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Init queue
        q = deque()
        # Append the pre-checked non-null root
        q.append(root)

        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # After we replaced the last queue with the next layer nodes;
            # we then increment the depth with 1
            depth += 1
        # Once donce looping through the nodes and its children;
        # the q becomes an empty list and is falsy; so lets return
        # the depth variable
        return depth
                


