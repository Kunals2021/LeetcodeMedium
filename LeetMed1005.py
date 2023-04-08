# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Initialize a table to store whether each substring is a palindrome
        dp = [[False] * n for _ in range(n)]
        # Initialize variables for the start and end indices of the longest palindrome
        start, end = 0, 0
        # Iterate over the string from the end to the beginning
        for i in range(n - 1, -1, -1):
            # Iterate over the string from i to the end
            for j in range(i, n):
                # If the current substring is a palindrome, mark it as such in the table
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    # If the current palindrome is longer than the current longest, update the indices
                    if j - i > end - start:
                        start, end = i, j
        # Return the longest palindromic substring
        return s[start:end + 1]
    
# This code defines a Solution class with a longestPalindrome method that takes a string s as input
# and returns the longest palindromic substring of s. The method uses dynamic programming to solve the 
# problem in O(n^2) time and O(n^2) space.
# we first initialize a table dp to store whether each substring s[i:j+1] is a palindrome. 
# We then initialize variables start and end to store the start and end indices of the longest
# palindrome found so far.
# We then iterate over the string s from the end to the beginning and for each index i, we iterate 
# over the string from i to the end. We check whether the current substring s[i:j+1] is a palindrome
# by checking if the first and last characters match and if the substring between them is also a 
# palindrome (which we can look up in dp). If the current substring is a palindrome, we mark it as such 
# in dp and update the start and end indices if the current palindrome is longer than the current 
# longest.
# Finally, we return the longest palindromic substring by slicing the string s using the start 
# and end indices.

