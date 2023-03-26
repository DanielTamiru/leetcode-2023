from queue import Queue
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Implementing iterative BFS solution because searching in depth order will explore
        fewer (or as many) nodes and iterative generally consumes less memory
        """
        nodes = Queue()
        if root: nodes.put(root)

        depth = 0

        while not nodes.empty():
            depth += 1
            depth_size = nodes.qsize()

            for _ in range(depth_size):
                node = nodes.get()
                if not node.left and not node.right: 
                    return depth

                if node.left: nodes.put(node.left)
                if node.right: nodes.put(node.right)
            
        return depth