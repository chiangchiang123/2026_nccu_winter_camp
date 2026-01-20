accounts = [1000, 2500, 500, 8000, 150]
status = ["Active", "Active", "Inactive", "Active", "Frozen"]
transactions = [200, -3000, 500, -100, -200, 1000, -9000]
target_account_indices = [0, 1, 2, 0, 4, 3, 3]

fees_collected = 0
alerts = 0

for i in range(len(transactions)):
    amount = transactions[i]
    idx = target_account_indices[i]
    
    current_status = status[idx]
    
    if current_status == "Frozen":
        alerts = alerts + 1
        continue
    
    if current_status == "Inactive" and amount < 0:
        alerts = alerts + 1
        continue
        
    balance = accounts[idx]
    
    if amount < 0:
        if balance + amount >= 0:
            accounts[idx] = balance + amount
        else:
            fee = 15
            if balance >= 15:
                accounts[idx] = balance - fee
                fees_collected = fees_collected + fee
            else:
                accounts[idx] = 0
                fees_collected = fees_collected + balance
            
            alerts = alerts + 1
            status[idx] = "Frozen"
    else:
        if current_status == "Inactive":
            status[idx] = "Active"
            amount = amount - 50 
            fees_collected = fees_collected + 50
        
        accounts[idx] = accounts[idx] + amount

total_assets = 0
active_count = 0

for k in range(len(accounts)):
    total_assets = total_assets + accounts[k]
    if status[k] == "Active":
        active_count = active_count + 1

print(accounts)
print(fees_collected)
print(alerts, active_count)
