def maxArea(height):
    start = 0
    end = len(height) - 1
    max_capacity = 0
    
    while start < end:
        h = min(height[start], height[end])
        width = end - start
        current_capacity = h * width
        max_capacity = max(current_capacity, max_capacity)
        
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
            
    return max_capacity

height_array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Max Water Store Capacity:", maxArea(height_array))