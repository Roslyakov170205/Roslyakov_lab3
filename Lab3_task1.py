# Функция для поиска индекса первого вхождения товара в списке складских позиций

def find_index(products, target_item):
    # Перебираем все элементы списка
    for index in range(len(products)):
        # Проверяем, совпадает ли текущий элемент с искомым товаром
        if products[index] == target_item:
            return index  # Возвращаем индекс при первом совпадении
    return None  # Возвращаем None, если товар не найден


# Список товаров на складе
warehouse_items = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Товары для поиска в списке
search_items = ['банан', 'груша', 'персик']

for item in search_items:
    # Вызов функции для поиска индекса товара
    item_index = find_index(warehouse_items, item)

    # Проверяем результат поиска и выводим соответствующее сообщение
    if item_index is not None:
        print(f"Первое вхождение товара '{item}' имеет индекс {item_index}.")
    else:
        print(f"Товар '{item}' не найден в списке.")
