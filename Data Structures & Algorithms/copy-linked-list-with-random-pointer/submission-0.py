"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # create nodes
        curr = head
        rando = {}
        while curr:
            rando[curr] = Node(curr.val)
            curr = curr.next
        # link
        curr = head
        while curr:
            if curr.next:
                rando[curr].next = rando[curr.next]
            if curr.random:
                rando[curr].random = rando[curr.random]
            curr = curr.next
        return rando[head]
