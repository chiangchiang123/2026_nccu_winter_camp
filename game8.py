matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
found_val = 0
search_count = 0

for row in matrix:
    for num in row:
        search_count = search_count + 1

        if num % 2 == 0:
            found_val = num
            break           

    if found_val > 5:
        break

print("Count:", search_count)
print("Found:", found_val)
