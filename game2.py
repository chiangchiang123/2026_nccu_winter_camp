grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

score = 0
x = 0
y = 0
mode = 1 
history = []

for i in range(10):
    current_val = grid[y][x]
    history.append(current_val)
    
    if mode == 1:
        score = score + current_val
        if current_val % 2 == 0:
            x = x + 1
        else:
            y = y + 1
    
    elif mode == -1:
        score = score - current_val
        if current_val % 3 == 0:
            y = y - 1
        else:
            x = x + 1

    if x > 3:
        x = 0
        y = y + 1
        mode = mode * -1
    
    if y > 3:
        y = 0
        x = 0 
        score = score + 50
        mode = 1

    if x < 0:
        x = 3
    if y < 0:
        y = 3

grid[1][1] = 99
grid[2][2] = 88

checksum = 0
for row in grid:
    for num in row:
        if num > 10:
            checksum = checksum + 1

print(history)
print(score)
print(checksum)
