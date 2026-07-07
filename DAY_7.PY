def addToArrayForm(num, k):
    answer = []
    p = len(num) - 1
    carry = 0
    
    while p >= 0 or k > 0 or carry > 0:
        num_val = 0
        if p >= 0:
            num_val = num[p]
            
        digit = k % 10
        total_sum = num_val + digit + carry
        
        answer.append(total_sum % 10)
        carry = total_sum // 10
        
        p -= 1
        k = k // 10
        
    answer.reverse()
    return answer

print(addToArrayForm([1, 2, 0, 0], 34))