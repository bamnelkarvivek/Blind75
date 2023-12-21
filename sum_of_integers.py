class Solution(object):
    def getSum(self,a,b):
        """

        :param a: int
        :param b: int
        :return: int
        """
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:
            a ,b = (a ^ b) & mask ,((a & b) << 1) & mask

        return a if a <= MAX else ~(a ^ mask)

x= Solution()
result = x.getSum(2,3)
print(result)
