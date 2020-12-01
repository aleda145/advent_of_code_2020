file = open("input","r")
expenses = []
for expense in file: 
    expenses.append(int(expense))

for expense_first in expenses:
    for expense_second in expenses:
        for expense_third in expenses:
            if expense_first+expense_second+expense_third==2020:
                print(expense_first*expense_second*expense_third)
