from typing import List

# ---------------------------------- Problem --------------------------------- #
# URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# --------------------------------- Solution --------------------------------- #


def twoSum(self, nums, target):
    cache = {}

    for i, num in enumerate(nums):
        remainder = target - num

    if remainder in cache:
        return [cache[remainder], i]

    cache[num] = i


# ---------------------------------- Problem --------------------------------- #
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# ----------------------------------- Notes ---------------------------------- #
# [7,1,5,3,6,4]
# to make max profit buy low and sell high
# profit must be positive -> if I choose a day to buy i would change start day only if it goes lower than current start day value.
# use a sliding window/ 2 pointer -> change left pointer if value of right is lower than left.

# --------------------------------- Solution --------------------------------- #


def maxProfit(self, prices: List[int]) -> int:
    left, max_profit = 0, 0

    for right in range(len(prices)):
        profit = prices[right] - prices[left]

        if prices[right] < prices[left]:
            left = right

        max_profit = max(profit, max_profit)

    return max_profit
