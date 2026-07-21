"""
LeetCode 242 - Valid Anagram

Approach 1:
- We can use the sorted() method to solve this problem.
- Example:
    sorted("anagram") == sorted("nagaram")
- Time Complexity: O(n log n)
- Space Complexity: O(n)

Approach 2 (Best):
- Count the frequency of each character.
- Increase the count for characters in the first string.
- Decrease the count for characters in the second string.
- If all counts become 0, the strings are anagrams.
- Time Complexity: O(n)
- Space Complexity: O(1) (for lowercase English letters)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Create a frequency array for 26 lowercase letters.
        count = [0] * 26

        # Count each character in the first string.
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Remove the count using the second string.
        for c in t:
            count[ord(c) - ord('a')] -= 1

        # If every value is 0, the strings are anagrams.
        return count == [0] * 26