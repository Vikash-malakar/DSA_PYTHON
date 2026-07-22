from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        if not nums:
            return [-1, -1]
            
        first = findBound(True)
        
        if first == -1:
            return [-1, -1]
            
        last = findBound(False)
        
        return [first, last]

if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {sol.searchRange(nums1, target1)}")
    
    # Test case 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {sol.searchRange(nums2, target2)}")
    
    # Test case 3
    nums3 = []
    target3 = 0
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {sol.searchRange(nums3, target3)}")