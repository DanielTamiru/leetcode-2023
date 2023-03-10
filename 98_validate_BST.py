from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Iteratively perform inorder traversal and check for strict increasing order
        """
        last_val = -inf
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= last_val: return False
            last_val = root.val
            root = root.right

        return True