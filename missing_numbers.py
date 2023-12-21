class Solution(object):
    def missingNumber(self, nums):
        """

        :param nums: List[int]
        :return: int
        """

        n = len(nums)
        expected_sum = n * (n+1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum

x= Solution()
result = x.missingNumber([3,0,1])
print(result)