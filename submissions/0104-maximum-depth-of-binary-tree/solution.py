# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
# O(n) - time complexity
# O(n) - space complexity
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if (root is None):
    #         return 0

    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# provide bfs soln

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     q = deque([root, None])
    #     if root is None:
    #         return 0

    #     depth = 0
    #     while q:
    #         node = q.popleft()
            
    #         if (node is None):
    #             depth += 1
    #             if q:
    #                 q.append(None)
    #             continue

    #         if (node.left):
    #             q.append(node.left)
            
    #         if (node.right):
    #             q.append(node.right)
        
    #     return depth

# provide iterative dfs solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        maxD = 0

        while (stack):
            node, depth = stack.pop()
            
            if node:
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                maxD = max(maxD, depth)

        return maxD

            

