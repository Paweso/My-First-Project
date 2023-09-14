bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

print("Earned amount:")
print(f"Bubblegum: ${bubblegum}")
print(f"Toffee: ${toffee}")
print(f"Ice cream: ${ice_cream}")
print(f"Milk chocolate: ${milk_chocolate}")
print(f"Doughnut: ${doughnut}")
print(f"Pancake: ${pancake}")

earned_amount = 0.0 + bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

print(f"Income: ${earned_amount}")

cleaner = 850
vendor = 1120
manager = 1300
loader = 900

electricity = 100
municipal_service = 90
security = 30
staff_expenses = int(input("Staff expenses: "))
other_expenses = int(input("Other expenses: "))
net_income = earned_amount - staff_expenses - other_expenses
print(f"Net income: ${net_income}")
