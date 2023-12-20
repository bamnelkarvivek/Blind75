class Solution(object):
    def threeSum(self,nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result


x= Solution()
result = x.threeSum([-1,0,1,2,-1,-4])
print(result)