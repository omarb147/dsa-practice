from typing import Tuple, List

# ---------------------------------- Problem --------------------------------- #
# URL - https://leetcode.com/problems/daily-temperatures/
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
# is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# ---------------------------- Consideration Notes --------------------------- #
# # [73, 74, 75,72 ,71, 69, 72, 76, 73
# [1, 1, 4, 2, 1, 1, 0, 0 ]
# for each value - loop until we find a greater value. (O(n^2))
# mon_stack = [(val,index),72,71]
# check stack each time
# [0,0,1,1,2]

# --------------------------------- Solution --------------------------------- #

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    mono_stack: List[Tuple[int, int]] = []
    answer = [0] * len(temperatures)

    for index in range(len(temperatures) - 1, -1, -1):
        val = temperatures[index]

        # maintain monotonic stack property
        while mono_stack and val >= mono_stack[-1][0]:
            mono_stack.pop()

        if len(mono_stack) == 0:
            answer[index] = 0
        else:
            answer[index] = mono_stack[-1][1] - index

        mono_stack.append((val, index))

    return answer
