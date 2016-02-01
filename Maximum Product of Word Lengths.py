__author__ = 'Martin'

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        flag = []
        lens = []
        for word in words:
            record = 0
            for c in word:
                shift = ord(c) - ord('a')
                record = record | (1 << shift)
            flag.append(record)
            lens.append(len(word))
        max = 0
        for i in range(len(flag)):
            for j in range(i+1, len(flag)):
                if flag[i] & flag[j] == 0:
                    if lens[i] * lens[j] > max:
                        max = lens[i] * lens[j]
        return max

s = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(s.maxProduct(words))