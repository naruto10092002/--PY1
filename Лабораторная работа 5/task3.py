# from random import sample
from random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) < 15:
        list_.append(randint(-10, 10))
        list_ = list(set(list_))

    return list_
    # return sample(range(-10, 11), k=15)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
