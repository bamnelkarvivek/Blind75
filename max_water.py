class Solution(object):
    def maxArea(self,height):
        """

        :param height: List[int]
        :return: int
        """
        max_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            container_height = min(height[left],height[right])
            max_water = max(max_water, container_height*width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

x= Solution()
result = x.maxArea([1,8,6,2,5,4,8,3,7])
print(result)

