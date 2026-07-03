class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        first_term = 0
        second_term = 1

        for i in range(1, n + 1):
            third_term = first_term + second_term
            first_term = second_term
            second_term = third_term

        return first_term


s = Solution()
print(s.fib(0))   # 0
print(s.fib(1))   # 1
print(s.fib(5))   # 5
print(s.fib(10))  # 55
