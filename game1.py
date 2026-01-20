stock = {
    "A001": 5,
    "A002": 2,
    "B001": 10,
    "C001": 0
}

prices = {
    "A001": 100,
    "A002": 200,
    "B001": 50,
    "C001": 300
}

orders = [
    ["A001", 3],
    ["A002", 3],
    ["B001", 5],
    ["C001", 1],
    ["A001", 2],
    ["D999", 1]
]

revenue = 0
shipping_fee = 0
failed_orders = []
vip_customer = True
total_items_sold = 0

for order in orders:
    item_code = order[0]
    quantity = order[1]
    
    if item_code not in stock:
        failed_orders.append(item_code)
        continue

    available = stock[item_code]
    
    if available >= quantity:
        cost = prices[item_code] * quantity
        
        stock[item_code] = available - quantity
        
        if vip_customer:
            if cost >= 500:
                cost = int(cost * 0.9)
            elif cost >= 200:
                cost = cost - 20
        
        revenue = revenue + cost
        total_items_sold = total_items_sold + quantity
        
        if quantity < 3:
            shipping_fee = shipping_fee + 10
        else:
            shipping_fee = shipping_fee + 5

    else:
        if available > 0:
            actual_qty = available
            cost = prices[item_code] * actual_qty
            stock[item_code] = 0
            
            revenue = revenue + cost
            total_items_sold = total_items_sold + actual_qty
            shipping_fee = shipping_fee + 10
            
            failed_orders.append(item_code + "_PARTIAL")
        else:
            failed_orders.append(item_code)

final_balance = revenue - shipping_fee

if total_items_sold > 10:
    final_balance = final_balance + 100

print(stock)
print(failed_orders)
print(final_balance)
