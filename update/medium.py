nums = list(range(10))
target = 3

low = 0
high = len(nums)

count = 0

while high >= low:
    mid = (high + low) // 2
    
    count = count + 1

    if nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        break

print(count)
