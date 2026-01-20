inventory = [10, 20, 30, 40, 50]
check_log = []

for item in inventory:
    if item < 35:
        item = 0
    check_log.append(item)

for i in range(len(inventory)):
    if inventory[i] > 35:
        inventory[i] = 99

total = 0
for x in inventory:
    total = total + x

print("Log:", check_log)
print("Inventory:", inventory)
print("Total:", total)
