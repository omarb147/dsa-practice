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