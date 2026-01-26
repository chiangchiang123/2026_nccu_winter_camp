x = 1
for i in range(1, 5):
    x = x * i
    if i % 2 == 0:
        x = x + i

y = 0
while x > 1:
    y = y + 1
    x = x // 2

print(y)