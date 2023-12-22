def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j] + 1)

    return max(dp)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = length_of_lis(nums)
