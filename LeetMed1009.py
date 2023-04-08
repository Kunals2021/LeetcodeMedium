# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []  # Initialize an empty list to store the final result
        def backtrack(S='', left=0, right=0):  # Define a helper function to generate all combinations recursively
            if len(S) == 2 * n:  # Base case: if the length of the string equals to 2*n, add it to the result
                res.append(S)
                return
            if left < n:  # If the number of left parentheses is less than n, add a left parenthesis and increment the counter
                backtrack(S+'(', left+1, right)
            if right < left:  # If the number of right parentheses is less than the number of left parentheses, add a right parenthesis and increment the counter
                backtrack(S+')', left, right+1)
        backtrack()  # Call the helper function with default parameters
        return res  # Return the result list

# This uses backtracking to generate all combinations of well-formed parentheses. 
# The function takes an integer n and returns a list of strings, each representing a 
# combination of well-formed parentheses with n pairs. The backtrack function is a helper
# function that takes four arguments: ans (a list to store the generated combinations), 
# cur (a string representing the current combination), open_ (an integer representing the number of 
# open parentheses in the current combination), and close_ (an integer representing the number 
# of close parentheses in the current combination). The function checks if the length of the 
# current combination is equal to 2 times n. If it is, the current combination is added to ans 
# and the function returns. Otherwise, the function checks if it's possible to add an open 
# parenthesis to the current combination (i.e., if the number of open parentheses is less than n). 
# If it is, the function calls itself recursively with the updated cur and open_ values. 
# Similarly, the function checks if it's possible to add a close parenthesis to the current 
# combination (i.e., if the number of close parentheses is less than the number of open parentheses). 
# If it is, the function calls itself recursively with the updated cur and close_ values. 
# Finally, the generateParenthesis function initializes an empty list ans, calls the backtrack 
# function with initial values for cur, open_, and close_, and returns ans.