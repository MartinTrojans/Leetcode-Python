from copy import deepcopy

__author__ = 'Martin'

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.df(input)

    def df(self, input):
        if input.isnumeric():
            return [int(input)]
        else:
            res = []
            for i in range(len(input)):
                if input[i] == '+':
                    for m in self.df(input[:i]):
                        for n in self.df(input[i+1:]):
                            res.append(m + n)
                elif input[i] == '-':
                    for m in self.df(input[:i]):
                        for n in self.df(input[i+1:]):
                            res.append(m - n)
                elif input[i] == '*':
                    for m in self.df(input[:i]):
                        for n in self.df(input[i+1:]):
                            res.append(m * n)
            return res
    '''
        stack1 = []
        stack2 = []
        for i in range(len(input)-1, -1, -1):
            stack1.append(input[i])
        return self.df(stack1, stack2)

    def df(self, stack, store):
        if len(stack) == 1:
            return stack.pop()
        else:
            res = []
            num1 = stack.pop()
            op = stack.pop()
            store.append(num1)
            store.append(op)
            for i in self.df(deepcopy(stack), deepcopy(store)):
                res += self.cal(i, deepcopy(store))
            store.pop()
            store.pop()
            num1 = int(num1)
            num2 = int(stack.pop())
            if op == "-":
                tres = num1 - num2
            elif op == "+":
                tres = num1 + num2
            elif op == "*":
                tres = num1 * num2
            stack.append(str(tres))

            for i in self.df(stack, store):
                res += self.cal(i, store)
            return res

    def cal(self, i, store):
        stack = [i]
        while len(store) > 1:
            stack.append(store.pop())
            stack.append(store.pop())
            while len(stack) > 1:
                num1 = int(stack.pop())
                op = stack.pop()
                num2 = int(stack.pop())
                if op == "-":
                    tres = num1 - num2
                elif op == "+":
                    tres = num1 + num2
                elif op == "*":
                    tres = num1 * num2
                stack.append(str(tres))
        return [stack[0]]
    '''

    '''
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
           if lo == hi:
               return [nums[lo]]
           return [ops[i](a, b)
                   for i in xrange(lo, hi)
                   for a in build(lo, i)
                   for b in build(i + 1, hi)]
        return build(0, len(ops))

    def diffWaysToCompute(self, input):
        return [eval(`a`+c+`b`)
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

    def diffWaysToCompute(self, input):
        return [eval(`a`+c+`b`)
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
    '''

s = Solution()
print(s.diffWaysToCompute("2*3-4+5"))