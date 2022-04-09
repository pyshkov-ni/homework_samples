# Приведем список покупок в магазине

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди
#   а. Вставьте рыбу между горошком и рисом
#   b. Добавьте фрукты из списка fruits в конец списка shop_list

fruits = ['Яблоко', 'Апельсин', 'Клубника']

#   c. Удалите из списка shop_list картофель
#   d. Какими по счету стоят хлеб и апельсин? Выведети номера на консоль в формате
#   Номер "продукта" в списке - N 

# Решение а.
shop_list.insert(shop_list.index('Рис'), 'Рыба')
print('Пункт a. -', shop_list)

# Решение b.
shop_list.extend(fruits)
print('Пункт b. -', shop_list)

# Решение c.
shop_list.remove('Картофель')
print('Пункт c. -', shop_list)

# Решение d.
print('Пункт d.')
print('Номер хлеба в списке -', shop_list.index('Хлеб') + 1)
print('Номер апельсина в списке -', shop_list.index('Апельсин') + 1)
