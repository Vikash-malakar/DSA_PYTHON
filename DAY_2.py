class Solution:
    def power(self, n):
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            while n % 2 == 0:
                n = n // 2
            if n == 1:
                return True
            else:
                return False


s = Solution()
print(s.power(10))
print(s.power(16))
print(s.power(1))
print(s.power(0))
