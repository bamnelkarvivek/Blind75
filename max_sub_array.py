class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            current_sum = max(num, current_sum+num)
            max_sum = max(current_sum, max_sum)
        return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
x = Solution()
result = x.maxSubArray(nums)
print(result)