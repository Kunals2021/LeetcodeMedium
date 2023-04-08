# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes 
# (i.e., only nodes themselves may be changed.)
from typing import List, Optional, ListNode
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, return the head
        if not head or not head.next:
            return head
        
        # Save the reference to the next pair of nodes
        new_head = head.next.next
        
        # Swap the current pair of nodes
        prev_node = head
        curr_node = head.next
        curr_node.next = prev_node
        prev_node.next = self.swapPairs(new_head)
        
        # Return the new head of the swapped pairs
        return curr_node

# The swapPairs function takes the head of a singly-linked list as input and returns the head 
# of the list with every two adjacent nodes swapped. The function first checks if the list is empty 
# or has only one node. If so, it returns the head unchanged.
# If the list has at least two nodes, the function saves a reference to the next pair of nodes 
# after the current pair. It then swaps the current pair of nodes by setting the next pointer 
# of the second node to the first node and setting the next pointer of the first node to the 
# recursively swapped next pair of nodes. Finally, the function returns the new head of the 
# swapped pairs.
