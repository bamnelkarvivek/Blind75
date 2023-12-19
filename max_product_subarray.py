class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        if not nums:
            return 0

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, num * max_product)
            min_product = min(num, num * min_product)
            result = max(result, max_product)
        return result


nums = [2,3,-2,4]

x = Solution()
result = x.maxProduct(nums)
print(result)
