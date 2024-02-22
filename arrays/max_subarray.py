# ---------------------------------- Problem --------------------------------- #
# URL: https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# ----------------------------------- Notes ---------------------------------- #
# Brute force -> check every subarray starting at n and compare to largest curr sum O(n^2)
# negative numbers mean that sliding window would't work as it could reduce before increasing
# When would you discard looking at a given subarray.
# any subarray that is negative will detract from the overall sum so we can always discard negative subarrays.


# --------------------------------- Solution --------------------------------- #
from typing import List


def maxSubArray(nums: List[int]) -> int:
    l, max_value = 0, max(nums)
    curr_array = nums[0]

    for r in range(1, len(nums)):
        while curr_array < 0 and l <= r:
            curr_array -= nums[l]
            l += 1

        curr_array += nums[r]

        if l < r:
            max_value = max(max_value, curr_array)

    return max_value
