"""
Question:
Find the contiguous subarray within an array (containing at least one
number) that has the largest sum.
For example, given the array [2, 1, –3, 4, –1, 2, 1, –5, 4],
The contiguous array [4, –1, 2, 1] has the largest sum = 6.
"""


from curses.ascii import SO


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
    # def maxSubArray(self, nums: 'List[int]') -> 'int':
        """
        O(n) runtime, O(1) space – Dynamic programming
        """
        max_ending_here, max_so_far = nums[0], nums[0]
        for i in range(1, len(nums)):
            # wqs greedy method, or the dp with memorize
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far

test=[2, 1, -3, 4, -1, 2, 1, -5, 4]
res = Solution().maxSubArray(test)
# print(f"the res is")
print(f"{res = }")