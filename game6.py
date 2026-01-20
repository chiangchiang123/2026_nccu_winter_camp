points = 850
level = "Standard"
bonus = 0

if points >= 1000:
    level = "Gold"
elif points >= 500:
    level = "Silver"
elif points >= 800:
    level = "Platinum"
else:
    level = "Bronze"

if level == "Silver":
    bonus = 100
    if points > 800:
        bonus = bonus + 50

if level == "Platinum":
    bonus = 500

print("Level:", level)
print("Bonus:", bonus)
