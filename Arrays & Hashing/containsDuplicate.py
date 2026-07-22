# LeetCode 217. Contains Duplicate
# Difficulty: Easy
#
# Approach:
# - Use a hash set to store the numbers we have already seen.
# - Traverse the array once.
# - If the current number is already in the set, return True.
# - Otherwise, add it to the set.
#
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # A set allows O(1) average-time lookup.
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False
        
           
        