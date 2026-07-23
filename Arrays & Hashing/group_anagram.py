"""
LeetCode 49 - Group Anagrams

Approach:
- Use a dictionary to group words.
- Sort each word to create a key.
- Words with the same sorted key are anagrams.
- Return all the grouped words.

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        # Dictionary to store grouped anagrams
        groups = defaultdict(list)

        # Process each word
        for word in strs:
            # Create a key by sorting the characters
            key = "".join(sorted(word))

            # Add the word to its matching group
            groups[key].append(word)

        # Return all groups
        return list(groups.values())