from queue import Queue
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_averages = []

        nodes = Queue()
        nodes.put(root)

        while not nodes.empty():
            count = nodes.qsize()
            val_sum = 0

            for _ in range(count): # for node in level:
                node = nodes.get()
                if node.left: nodes.put(node.left)
                if node.right: nodes.put(node.right)
                
                val_sum += node.val

            level_averages.append(val_sum/count)

        return level_averages