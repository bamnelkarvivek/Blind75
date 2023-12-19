class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            # If the element is already in the set, it's a duplicate
            if num in seen:
                return True

            # Add the element to the set
            seen.add(num)

        # If the loop completes, there are no duplicates
        return False

x = Solution()
result = x.containsDuplicate(nums=[1,2,3,1])
print(result)