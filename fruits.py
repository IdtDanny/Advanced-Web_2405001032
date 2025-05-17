fruits = {"Apple":1000, "Banana": 500, "Mango": 1200}

totalCost = 0

for name, price in fruits.items():
    print(f"{name} : {price}")
    totalCost += price * 2

print(f"The Total Cost is {totalCost} RWF")