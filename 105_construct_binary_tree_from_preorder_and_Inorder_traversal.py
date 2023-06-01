from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        - Root of tree is first node in preorder
        - Because keys in the list params are unique, everything to left of this number
          in inorder is in the root's left subtree and conversely for the right 
        """
        if not preorder: return None

        val = preorder[0]
        root = TreeNode(val)
        
        if len(preorder) == 1: return root
        
        inorder_idx = inorder.index(val)

        root.left = self.buildTree(preorder[1: 1 + inorder_idx], inorder[:inorder_idx])
        root.right = self.buildTree(preorder[1 + inorder_idx:], inorder[1 + inorder_idx:])

        return root
