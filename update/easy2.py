nums = list(range(10))
found_val = 0
search_count = 0

for num in nums:
    search_count += 1

    if num % 2 == 0:
        found_val = num

    if found_val > 5:
        break

print(search_count)
print(found_val)
