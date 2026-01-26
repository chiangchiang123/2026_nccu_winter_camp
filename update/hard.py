def calculate(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        total = 0
        for i in range(1, n//2 + 1):
            total += i
        return total + calculate(n - 1)
    else:
        return calculate(n - 2) * 2

nums = [2, 3, 5, 6]
result = 0

for x in nums:
    result += calculate(x)

print(result)
