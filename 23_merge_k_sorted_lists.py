class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from queue import PriorityQueue
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue() # use priority queue (generalization of 2 list merge) 

        for idx, head in enumerate(lists): 
            if head:
                q.put((head.val, idx, head)) # pq of tuples: (node val, list idx, node)
                lists[idx] = head.next

        result = prevnode = None

        while not q.empty():
            next_node = q.get()

            if prevnode is None: # set result head
                result = prevnode = next_node[2]
            else:
                prevnode.next = next_node[2]
                prevnode = prevnode.next

            # update head of list of list that was just removed
            new_head = lists[next_node[1]]
            if new_head: 
                q.put((new_head.val, next_node[1], new_head))
                lists[next_node[1]] = new_head.next
            
        return result

        
