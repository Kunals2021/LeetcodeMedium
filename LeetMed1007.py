# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty result list
        result = []
        # Sort the array
        nums.sort()
        # Iterate over the array
        for i in range(len(nums)):
            # If the current element is greater than 0, we can break the loop since no triplet sum can be 0
            if nums[i] > 0:
                break
            # If the current element is the same as the previous element, skip it to avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Initialize two pointers to the start and end of the remaining array
            left, right = i+1, len(nums)-1
            # Iterate over the remaining array with the two pointers
            while left < right:
                # Calculate the sum of the three elements
                current_sum = nums[i] + nums[left] + nums[right]
                # If the sum is 0, append the triplet to the result list and move the two pointers towards the middle
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate elements to avoid duplicate triplets
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                # If the sum is less than 0, move the left pointer towards the right
                elif current_sum < 0:
                    left += 1
                # If the sum is greater than 0, move the right pointer towards the left
                else:
                    right -= 1
        # Return the result list
        return result

# The method takes an array of integers nums as input and returns a list of all unique triplets whose 
# sum is 0. The method first sorts the array to simplify the process of skipping duplicate elements. 
# Then it iterates over the array with a for loop, checking whether each element is greater than 0, 
# and skipping duplicate elements. For each element that is not greater than 0 and not a duplicate, 
# it initializes two pointers to the start and end of the remaining array and iterates over the 
# remaining array with the two pointers. At each iteration, it calculates the sum of the three elements 
# and moves the two pointers towards the middle if the sum is 0. If the sum is less than 0, it moves 
# the left pointer towards the right. If the sum is greater than 0, it moves the right pointer towards 
# the left. The method skips duplicate elements to avoid duplicate triplets, and returns the result list.