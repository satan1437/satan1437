from typing import List

import pytest


# https://leetcode.com/problems/two-sum/
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:  # noqa
		book = {}
		for indx, num in enumerate(nums):
			if target - num in book:
				return [book[target - num], indx]
			book[num] = indx


test_data = [
	([2, 7, 11, 15], 9, [0, 1]),
	([3, 2, 4], 6, [1, 2]),
	([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize('nums, target, expected', test_data)
def test_two_sum(nums, target, expected):
	assert Solution().twoSum(nums, target) == expected
