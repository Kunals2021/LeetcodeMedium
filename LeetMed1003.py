# Given a string s, find the length of the longest substring without repeating characters.
# 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to keep track of the last occurrence of each character
        last_occurrence = {}
        # Initialize two pointers, start and end, and the length of the longest substring, max_length
        start = 0
        max_length = 0
        
        # Loop through the string with the end pointer
        for end in range(len(s)):
            # If the current character is in the dictionary and its last occurrence is after the start pointer,
            # update the start pointer to the index after the last occurrence of the character
            if s[end] in last_occurrence and last_occurrence[s[end]] >= start:
                start = last_occurrence[s[end]] + 1
            # Update the last occurrence of the current character
            last_occurrence[s[end]] = end
            # Update the length of the longest substring
            max_length = max(max_length, end - start + 1)
        
        # Return the length of the longest substring
        return max_length

# We first initialize a dictionary last_occurrence to keep track of the last occurrence of each 
# character in the string. We also initialize two pointers, start and end, and the length of the 
# longest substring, max_length.
# We then loop through the string with the end pointer. For each character, we check if it is in 
# the last_occurrence dictionary and its last occurrence is after the start pointer. If so, we 
# update the start pointer to the index after the last occurrence of the character. We then update 
# the last occurrence of the current character in the last_occurrence dictionary and update the length 
# of the longest substring.
# After the loop is done, we return the length of the longest substring, which is stored in the 
# max_length variable.



