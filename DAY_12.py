def sorted_squares(nums):
    n = len(nums)
    
    ans = [0] * n
    
    start = 0
    end = n - 1
    pointer = n - 1
    
    while start <= end:
        start_sq = nums[start] ** 2
        end_sq = nums[end] ** 2
        
        
        if start_sq > end_sq:
            ans[pointer] = start_sq
            start += 1
        else:
            ans[pointer] = end_sq
            end -= 1
            
        pointer -= 1
        
    return ans

my_list = [-4, -1, 0, 3, 10]

result = sorted_squares(my_list)


print("Original List:", my_list)
print("Sorted Squares:", result)