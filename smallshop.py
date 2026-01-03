Earned_amount = {
    'Bubblegum': 202,
    'Toffee': 118, 
    'Ice cream': 2250,
    'Milk chocolate': 1680,
    'Doughnut': 1075,
    'Pancake': 80,
}
 
print('Earned_amount: ')
for item, price in Earned_amount.items():
    print(f"{item}: ${price}")
    
print(f"\nIncome: ${sum(Earned_amount.values())}")
 
staff = int(input("Staff expenses: \n"))
other_expenses = int(input("Other expenses: \n"))
 
net_income = sum(Earned_amount.values()) - staff - other_expenses
print('Net income: $',float(net_income), sep='')
