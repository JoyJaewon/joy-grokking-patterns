from typing import Optional

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next 
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_to_new = {}
        curr = head

        while curr:
            new_Node = Node(curr.val)
            old_to_new[curr] = new_Node
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]
        