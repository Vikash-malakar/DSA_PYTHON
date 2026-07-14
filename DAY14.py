def product_except_self(nums):
    n = len(nums)
    ans = [1] * n

    # Left Product
    curr = 1
    for i in range(n):
        ans[i] = curr
        curr = curr * nums[i]

    # Right Product
    curr = 1
    for i in range(n - 1, -1, -1):
        ans[i] = ans[i] * curr
        curr = curr * nums[i]

    return ans


nums = list(map(int, input("Enter numbers separated by space: ").split()))

result = product_except_self(nums)

print("Output:", result)