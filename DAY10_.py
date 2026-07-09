class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 0, 1]
    print(f"Input: {nums1}")
    print(f"Missing Number: {solution.missingNumber(nums1)}\n")

    nums2 = [0, 1]
    print(f"Input: {nums2}")
    print(f"Missing Number: {solution.missingNumber(nums2)}\n")

    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(f"Input: {nums3}")
    print(f"Missing Number: {solution.missingNumber(nums3)}")