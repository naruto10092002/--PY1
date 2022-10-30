def delete(list_, index=None):
    if index is None:
        index = len(list_) - 1                          # Аргументом по умолчанию выбираем индекс последнего элемента
    list_ = list_[:]                                    # Копируем список
    result = list_[:index] + list_[index + 1:]          # Соединяем два среза без удаляемого элемента

    return result


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
