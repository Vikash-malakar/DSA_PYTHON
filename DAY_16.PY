class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = -1
        second_max = -1
        max_index = -1
        
        for i in range(len(nums)):
            if max_val < nums[i]:
                second_max = max_val
                max_val = nums[i]
                max_index = i
            elif second_max < nums[i]:
                second_max = nums[i]
                
        if second_max * 2 <= max_val:
            return max_index
        return -1