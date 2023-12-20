class Solution(object):
    def findMin(self,nums):
        """

        :param nums: List[int]
        :return: int
        """
        low,high = 0, len(nums)-1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1

        return nums[low]

x= Solution()
result = x.findMin([3,4,5,1,2])
print(result)