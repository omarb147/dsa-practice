# ---------------------------------- Problem --------------------------------- #
# URL : https://leetcode.com/problems/product-of-array-except-self/editorial/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].=
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


# ----------------------------- Notes on problem ----------------------------- #
# [1, 2, 3, 4]
# using division could calculate the product of all then divide at each index
# do 2 prefix sums -> store values to left and right of number at index
# multiply to find out sum excluding number
# left = [1, 1, 2, 6]
# right = [24,12,4,1]
# ans =[]

# --------------------------------- Solution --------------------------------- #
from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    left, right = [1] * len(nums), [1] * len(nums)
    ans = [0] * len(nums)

    # Calculate Left product for index
    for index in range(1, len(nums)):
        left[index] = nums[index - 1] * left[index - 1]

    # Calculate Right product for index
    for index in range(len(nums) - 2, -1, -1):
        right[index] = nums[index + 1] * right[index + 1]

    for index in range(len(nums)):
        ans[index] = left[index] * right[index]

    return ans
