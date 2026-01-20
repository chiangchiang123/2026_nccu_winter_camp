x = 10
y = 5
z = 0

result_1 = x > 5 and y < 3 or z == 0
result_2 = (x > 5 or y < 3) and z == 0

val_a = x // 3 * 2  
val_b = x + y % 2 * 5 

status = "FAIL"
if result_1 and val_a > 5:
    status = "Pass A"
elif result_1 and val_b > 10:
    status = "Pass B"
else:
    status = "Pass C"

print(result_1, result_2)
print(val_a, val_b)
print(status)
