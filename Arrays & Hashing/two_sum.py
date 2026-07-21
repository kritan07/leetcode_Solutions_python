"""
LeetCode 1. Two Sum

Approach:
- Brute Force:
  Check every pair of numbers.
  Time Complexity : O(n²)
  Space Complexity: O(1)

- Optimal (Hash Map):
  Store visited numbers in a dictionary.
  For each number, calculate its complement (target - num).
  If the complement already exists, return both indices.

  Time Complexity : O(n)
  Space Complexity: O(n)

Why use Hash Map?
- Only one traversal of the array.
- Dictionary lookups are O(1) on average.
- More efficient than checking every pair.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # key -> number
        # value -> index
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index

        return []