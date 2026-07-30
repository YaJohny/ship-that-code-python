item = input()
qty = int(input())
unit_price = float(input())
total = qty * unit_price

print(f"Item: {item}")
print(f"Quantity: {qty}")
print(f"Total: ${total:.2f}")
