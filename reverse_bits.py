class Solution(object):
    def reverseBits(self,n):
        """

        :param n: int
        :return: int
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return  result

x= Solution()
result = x.reverseBits(0b00000010100101000001111010011100)
print(result)