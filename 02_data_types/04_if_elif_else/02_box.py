# Заданы размеры коробки box_x, box_y и товара product_x, product_y
# Определить, поместится ли товар в коробке (габариты товара параллельны размеру коробки)
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

box_x, box_y = 10, 7
product_x, product_y = 8, 9

# проверить для
# product_x, product_y = 9, 8
# product_x, product_y = 6, 8
# product_x, product_y = 8, 6
# product_x, product_y = 3, 4
# product_x, product_y = 11, 9
# product_x, product_y = 9, 11

# Раскомментируйте нужную строку

print('*'*7, 'Поместиться ли товар в коробке?'.upper(), '*'*7)
print('Размер коробки:', box_x, 'на', box_y)
print('Размер товара:', product_x, 'на', product_y)

# Решение 1
# if product_x <= box_x:
#     if product_y <= box_y:
#         print('ДА!')
#     else: 
#         print('НЕТ!')
# else:
#     print('НЕТ!')

<<<<<<< HEAD
# # Решение 2
# if product_x <= 0 or product_y <= 0:
#     print('Размер товара не может быть меньше 0!')
# elif product_x > box_x:
#     print('НЕТ!')
# elif product_y > box_y:
#     print('НЕТ!')
# else:
#     print('ДА!')

# Решение 3
if product_x > box_x or product_y > box_y:
=======
# Решение 2
if product_x <= 0 or product_y <= 0:
    print('Размер товара не может быть меньше 0!')
elif product_x > box_x:
    print('НЕТ!')
elif product_y > box_y:
>>>>>>> f3d68a9 (a. 02_box - добавил решение 3)
    print('НЕТ!')
else:
    print('ДА!')

# Решение 3
if product_x > box_x or product_y > box_y:
    print('НЕТ!')
else:
    print('ДА!')
