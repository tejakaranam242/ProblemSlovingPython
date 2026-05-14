amount = float(input())
d = 0.05 if amount < 1000 else 0.1 if amount < 5000 else 0.15
print(f"{amount-amount*d:.2f}")