money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    money_capital = money_capital + salary - spend

    if money_capital < 0:
        break

    month += 1
    spend *= 1 + increase       # the complex percent

print(month)
