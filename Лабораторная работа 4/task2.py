DEFAULT_COUNT = 0                                       # Список и словарь копируются, поскольку это изменяемые типы,
                                                        # которые передаются по ссылке,
                                                        # поэтому я оставил соответствующие строки в коде
def get_count_char(str_):
    str_ = str_[:]                                      # Копируем строку
    new_str = str_.lower()                              # Приводим к нижнему регистру
    dict_ = dict()                                      # Создаём пустой словарь

    for i in new_str:                                   # Идём по каждому символу из строки
        if not (i.isalpha()):
            continue                                    # Игнорируем небуквенные символы
        dict_[i] = dict_.get(i, DEFAULT_COUNT) + 1      # Заполняем словарь

    return dict_


def get_percentage(dict_):                              # Требуемая в п.5 функция
    list_items = list(dict_.items())
    new_dict = dict(list_items)                         # Копируем словарь
    total_symbols = sum(new_dict.values())              # Находим суммарное число буквенных символов

    for i in new_dict:
        new_dict[i] /= total_symbols                    # Выражаем частоту появления в долях единицы,...
        new_dict[i] *= 100                              # ... приводим к процентам...
        new_dict[i] = round(new_dict[i], 2)             # ... и округляем

    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
# print(get_percentage(get_count_char(main_str)))
