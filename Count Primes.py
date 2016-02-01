import math

__author__ = 'Martin'

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime  = [True for i in range(n)]
        i = 2
        m = int(n**0.5)
        while i <= m:
            if isPrime[i] is False:
                i += 1
                continue
            j = i * i
            while j < n:
                isPrime[j] = False
                j += i
            i += 1
        i = 2
        count = 0
        while i < n:
            if isPrime[i] is True:
                count += 1
            i += 1
        return count

    '''
    def isPrime(self, n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        m = math.ceil(math.sqrt(n))
        i = 0
        while i <= m:
            if n % i == 0:
                return False
        return True
    '''

s = Solution()
print(s.countPrimes(25))