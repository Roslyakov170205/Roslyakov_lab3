# Функция для поиска общих участников из двух строк, содержащих списки участников с указанным разделителем

def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки на элементы по указанному разделителю и преобразуем их в множества
    group1_set = set(group1.split(delimiter))
    group2_set = set(group2.split(delimiter))

    # Находим пересечение двух множеств и сортируем результат
    common_members = sorted(group1_set.intersection(group2_set))

    return common_members


# Участники двух групп, указанные строками с разделителем "|"
group_one = "Иванов|Петров|Сидоров"
group_two = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем, отличным от запятой
print(find_common_participants(group_one, group_two, "|"))
