name = input()
salary = float(input())
total_sold = float(input())
bonus = total_sold * (15/100)
net_salary = salary + bonus

print('TOTAL = R$ %.2f' % net_salary)