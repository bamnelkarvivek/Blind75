# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in complement_dict:
                return [complement_dict[complement],i]

            complement_dict[num] = i

        return None


x = Solution()
result = x.twoSum(nums=[2, 7, 11, 15], target=9)
print(result)
