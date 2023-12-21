class Solution(object):
    def hammingWeight(self, n):
        """

        :param n: int
        :return: int
        """
        hammingWeight = 0
        while n:
            hammingWeight += n & 1
            n >>= 1
        return hammingWeight

x= Solution()
n = 0b000000000000000000000000001011
result = x.hammingWeight(n)
print(result)