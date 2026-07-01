class Solution:

    def num(self, n):

        if n < 0:
            return False

        original = n
        rev = 0

        while n > 0:
            d = n % 10
            rev = rev * 10 + d
            n = n // 10

        return rev == original


n = int(input("Enter any number: "))

obj = Solution()
print(obj.num(n))