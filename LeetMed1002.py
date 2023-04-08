# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored # in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the # # sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head for the result linked list
        dummy_head = ListNode(0)
        # Set a pointer to the dummy head
        curr_node = dummy_head
        # Initialize a carry variable to 0
        carry = 0
        
        # Loop through the linked lists until both of them are None
        while l1 or l2:
            # Get the values of the current nodes, or 0 if the nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of the values and the carry
            total = val1 + val2 + carry
            # Calculate the new carry
            carry = total // 10
            # Set the value of the current node to the ones digit of the sum
            curr_node.next = ListNode(total % 10)
            # Move the pointer to the next node
            curr_node = curr_node.next
            # Move the pointers for the input linked lists, if they are not None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there is a carry after the last digit has been added, add a new node to the linked list
        if carry:
            curr_node.next = ListNode(carry)
        
        # Return the linked list starting from the second node (i.e., the one after the dummy head)
        return dummy_head.next

# We first create a dummy head for the result linked list, and set a pointer curr_node to it.
# We also initialize a variable carry to 0 to keep track of any carry-over values.
# We then loop through the input linked lists l1 and l2, adding the values of the corresponding nodes 
# and the carry value. We update the carry value and set the value of the current node in the result 
# linked list to the ones digit of the sum. We then move the pointer curr_node to the next node in 
# the result linked list, and move the pointers for the input linked lists if they are not None.
# After the loop is done, if there is still a carry value, we add a new node to the result linked 
# list with the carry value as its value.
# Finally, we return the linked list starting from the second node (i.e., the one after the dummy head),
# which is the actual result of adding the two input numbers represented as linked lists.