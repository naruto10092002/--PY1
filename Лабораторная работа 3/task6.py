list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

num = list_numbers[0]
max_pos = 0

for i in range(1, len(list_numbers), 1):        # finding the maximal value and its position in the list
    if list_numbers[i] > num:
        max_pos = i
        num = list_numbers[i]

last = list_numbers[-1]
list_numbers[max_pos], list_numbers[-1] = last, num

print(list_numbers)
