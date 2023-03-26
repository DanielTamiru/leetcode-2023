from queue import Queue
from collections import namedtuple
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

DepthNode = namedtuple('DepthNode', ['node', 'depth'])


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Implementing iterative BFS solution because searching in depth order will explore
        fewer (or as many) nodes and iterative generally consumes less memory
        """
        dnodes = Queue()
        if root: dnodes.put(DepthNode(root, 1))
        
        min_depth = 0
       
        while not dnodes.empty():
            dnode = dnodes.get()
            min_depth = max(min_depth, dnode.depth)
            left_child, right_child = dnode.node.left, dnode.node.right

            if not left_child and not right_child: break # min depth found!
            
            if dnode.node.left: dnodes.put(DepthNode(left_child, min_depth + 1))
            if dnode.node.right: dnodes.put(DepthNode(right_child, min_depth + 1))
        
        return min_depth# Definition for a binary tree node.
