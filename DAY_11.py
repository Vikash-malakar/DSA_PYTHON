class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
                
        return pointer


nums = [3, 2, 2, 3]
val = 3

sol = Solution()
k = sol.removeElement(nums, val)

print(k)
print(nums[:k])