source = "Python-Programming-2025"
buffer = ""
result = ""
key = 3
toggle = False

for char in source:
    if char == "-":
        if len(buffer) > 0:
            if toggle:
                result = result + buffer[::-1]
            else:
                result = result + buffer.upper()
        
        buffer = ""
        toggle = not toggle
        continue
    
    code = ord(char)
    
    if code >= 48 and code <= 57:
        num = int(char)
        if num % 2 == 0:
            buffer = buffer + str(num + 1)
        else:
            buffer = buffer + str(num - 1)
    
    elif code >= 65 and code <= 90:
        new_char = chr(code + 1)
        buffer = buffer + new_char
    
    elif code >= 97 and code <= 122:
        if len(buffer) < 2:
            buffer = buffer + char
        else:
            buffer = char + buffer 

if len(buffer) > 0:
    if toggle:
        final_part = ""
        for i in range(len(buffer)):
            if i % 2 == 0:
                final_part = final_part + buffer[i]
        result = result + final_part
    else:
        result = result + buffer

count_upper = 0
count_digits = 0

for c in result:
    if c >= "A" and c <= "Z":
        count_upper = count_upper + 1
    if c >= "0" and c <= "9":
        count_digits = count_digits + 1

print(result)
print(count_upper, count_digits)
