from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Child -> Parent approach:
    
        Iteratively, you need to explicitly distinguish
        encountering a node initially vs ecountering one after having
        explored any or all of its children. The easiest way to accomplish
        that would be by setting children to None, but mutating the tree
        is generally considered bad practice.

        Smart Traversal:

        Instead of putting checks in place to ensure the right order is
        achieved in the above approach, we literally perform an inorder
        traversal by repeatedly going as left as we can, then going one
        node to the right.
        """
        result = []
        stack = []
        
        while root or stack:
            # Go as left as you can
            while root is not None:
                stack.append(root)
                root = root.left
            # Go right one
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return result
