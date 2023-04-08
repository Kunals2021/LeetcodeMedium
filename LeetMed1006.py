# Container With Most Water
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) 
# and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains 
# the most water.
# Return the maximum amount of water a container can store.

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers to the start and end of the array
        left, right = 0, len(height) - 1
        # Initialize a variable to store the maximum area seen so far
        max_area = 0
        # Iterate over the array with the two pointers
        while left < right:
            # Calculate the current area using the shorter line and update the max area if necessary
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            # Move the pointer pointing to the shorter line towards the other end
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # Return the maximum area seen
        return max_area

# The method takes an array of integers height as input and returns the maximum amount of water 
# that can be stored in a container formed by two lines in the array. The method initializes two 
# pointers to the start and end of the array and iterates over the array with the two pointers. 
# At each iteration, it calculates the area of the container formed by the two lines and updates 
# the maximum area seen so far if necessary. Then it moves the pointer pointing to the shorter line 
# towards the other end, since moving the pointer pointing to the taller line will only decrease 
# the area of the container. Finally, it returns the maximum area seen.
# implementation of the maxArea method using two pointers solves the problem in O(n) time.
