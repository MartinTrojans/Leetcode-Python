__author__ = 'Martin'


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0;
        cow = 0;
        chs = [0 for i in range(len(secret))];
        flag = [1 for i in range(len(secret))];
        for i in range(len(secret)):
            chs[i] = secret[i];
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                flag[i] = 0
        i = 0
        while i < len(flag):
            if flag[i] == 0:
                del flag[i]
                del chs[i]
                guess = guess[0:i] + guess[i+1:]
            else:
                i += 1
        for i in range(len(guess)):
            if chs.__contains__(guess[i]):
                chs.remove(guess[i])
                cow += 1
        return str(bull) + "A" + str(cow) + "B"

s = Solution()
print(s.getHint("", ""))