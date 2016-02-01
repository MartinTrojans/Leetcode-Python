import heapq

__author__ = 'Martin'

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        size = len(primes)
        index = [0 for i in range(size)]
        vals = [0 for i in range(size)]
        res = [1]
        for i in range(1, n):
            for j in range(size):
                vals[j] = res[index[j]] * primes[j]
            res.append(min(vals))
            for j in range(size):
                if vals[j] == res[i]:
                    index[j] += 1
        return res[n-1]

    def nthSuperUglyNumber1(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

s = Solution()
print(s.nthSuperUglyNumber1(10, [2,3,5]))