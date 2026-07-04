def tribonacci(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    t0 = 0
    t1 = 1
    t2 = 1

    for i in range(3, n + 1):
        next_val = t0 + t1 + t2
        t0 = t1
        t1 = t2
        t2 = next_val

    return t2


n = int(input("Enter a number: "))
print("Tribonacci Number:", tribonacci(n))