def process_sequence(start, limit, step):
    seq = []
    curr = start
    while curr < limit:
        val = (curr * step) % 100
        
        if val == 0:
            val = 1
            
        if val % 2 == 0:
            val = val // 2
        else:
            val = val * 3 + 1
            
        if val > 50:
            val = val - 10
            
        seq.append(val)
        curr = curr + 1
    return seq

def filter_data(data_list, threshold):
    result = []
    skip_next = False
    
    for i in range(len(data_list)):
        if skip_next:
            skip_next = False
            continue
            
        val = data_list[i]
        
        if val > threshold:
            result.append(val)
        elif val == threshold:
            result.append(0)
            skip_next = True
        else:
            if i + 1 < len(data_list):
                next_val = data_list[i+1]
                if next_val > threshold:
                    result.append(val + next_val)
                else:
                    result.append(val)
            else:
                result.append(val)
                
    return result

list_a = process_sequence(1, 8, 3)
list_b = process_sequence(5, 10, 4)

combined = list_a + list_b
final_output = filter_data(combined, 20)

sum_val = 0
for x in final_output:
    sum_val = sum_val + x

print(list_a)
print(list_b)
print(final_output)
print(sum_val)
