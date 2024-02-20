# ---------------------------------- Problem --------------------------------- #
# URL: https://leetcode.com/problems/house-robber/
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# 
# ----------------------------------- Notes ---------------------------------- #
# [1,2,3,1]
# [2,1,1,2] ->
# [2,7,9,3,1] -> 2 or 7
# Can take either the path -> n+1 or (n+2 +n) for any N
# relation -> rob(n) = max(rob(n+2), rob(n+3))
# stack=[(0,0),(1,0),(2,1),(3,1),(4,4),(6,4),()]
# 
# --------------------------------- Solution --------------------------------- #

from functools import lru_cache
from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:

        @lru_cache
        def dp(n):
            if n > len(nums) - 1:
                return 0

            return max(dp(n + 1), (dp(n + 2) + nums[n]))

        return dp(0)
