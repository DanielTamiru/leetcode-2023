from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        In an iterative approach, you need to explicitly distinguish
        encountering a node initially vs ecountering one after having
        explored any or all of its children. Below, this is accomplished by
        mutating the tree, but depending on the context, that may be bad practice.
        """

        res = []

        node_stack = [root]
        while node_stack:

            node = node_stack.pop()
            if not node: continue
            left, right = node.left, node.right 

            if left or right: node_stack.extend([right, node, left])
            else: res.append(node.val)

            node.left = node.right = None
        
        return res

        