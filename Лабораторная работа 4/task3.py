def delete(list_, index=None):                          # Аналогично предыдущему: оставил копирование списка
    if index is None:
        index = len(list_) - 1                          # Аргументом по умолчанию выбираем индекс последнего элемента
    list_ = list_[:]                                    # Копируем список

    return list_[:index] + list_[index + 1:]            # Соединяем два среза без удаляемого элемента и возвращаем


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
