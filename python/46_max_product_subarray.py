"""
Question:
Find the contiguous subarray within an array of integers that has the
largest product. For example, given the array [2,3,-2,4], the contiguous
subarray [2,3] has the largest product = 6.
Example Questions Candidate Might Ask:
Q: Could the subarray be empty?
A: No, the subarray must contain at least one number.
"""


class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':
        # wqs the corner case or the base situation
        assert len(nums) > 0
        _max, _min, max_ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx = _max
            mn = _min
            _max = max(max(nums[i], mx * nums[i]), mn * nums[i])
            # wqs why need a double var name for _max, cause
            # wqs that value is used in below
            _min = min(min(nums[i], mx * nums[i]), mn * nums[i])
            max_ans = max(_max, max_ans)
        return max_ans

