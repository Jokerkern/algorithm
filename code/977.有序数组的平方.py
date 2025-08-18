#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        Answers = [0] * len(nums)
        i = len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                Answers[i] = nums[right] * nums[right]
                right = right - 1
            else:
                Answers[i] = nums[left] * nums[left]
                left = left + 1
            i = i - 1
        return Answers
# @lc code=end

