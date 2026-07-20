class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store:
        # key   -> number
        # value -> index of the number
        seen = {}

        # Traverse through the array
        for index, num in enumerate(nums):

            # Find the number needed to reach the target
            complement = target - num

            # If the complement already exists,
            # we have found the required pair
            if complement in seen:
                return [seen[complement], index]

            # Store the current number and its index
            seen[num] = index

        # This line will never be reached because
        # the problem guarantees exactly one solution.
        return []