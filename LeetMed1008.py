# Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
# that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Define the mapping of digits to letters
        digit_to_letter = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Define the recursive function to generate all combinations
        def backtrack(combination, digits):
            # Base case: if there are no more digits left to process, add the current combination
            if len(digits) == 0:
                result.append(combination)
            # Recursive case: for each possible letter corresponding to the current digit, continue the search
            else:
                for letter in digit_to_letter[digits[0]]:
                    backtrack(combination + letter, digits[1:])
        
        # Initialize the result and start the recursive search
        result = []
        if digits:
            backtrack("", digits)
        return result

# In this implementation, we first define a dictionary digit_to_letter that maps each digit to the 
# corresponding letters on a phone keypad. Then, we define a recursive function backtrack that takes 
# a current combination and the remaining digits to be processed, and generates all possible combinations
#  by trying out each possible letter corresponding to the current digit and continuing the search 
# recursively for the remaining digits.
# We initialize the result list and start the recursive search by calling backtrack with an empty
#  string as the initial combination and the input digits as the remaining digits to be processed.
#  Finally, we return the result list. If the input digits is an empty string, we simply return an 
# empty list as there are no possible combinations to generate.