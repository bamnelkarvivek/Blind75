class Solution(object):
    def longestCommonSubsequence(self,text1,text2):
        """

        :param text1: str
        :param text2: str
        :return: int
        """
        shorter_text = ""
        longer_text = ""
        index, count = 0, 0
        if len(text1) < len(text2):
            shorter_text = text1
            longer_text = text2
        else:
            shorter_text = text2
            longer_text = text1

        for i in range(len(shorter_text)):
            for j in range(index,len(longer_text)):
                if shorter_text[i] == longer_text[j]:
                    index = j + 1
                    count += 1
                    print(index, count)
                    print(shorter_text[i],longer_text[j])
                    break
        return count

text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
x= Solution()
result = x.longestCommonSubsequence(text1,text2)
print(result)