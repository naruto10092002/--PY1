src = not False and True or False and not True

# расставим скобки согласно приоритетам булевых операторов
# result = ((not False) and True) or (False and (not True))
# упростим оператор отрицания
# result = (True and True) or (False and False)
# упростим оператор И
# result = True or False
# упростим оператор ИЛИ
# result = True

result = True

print(src == result)
