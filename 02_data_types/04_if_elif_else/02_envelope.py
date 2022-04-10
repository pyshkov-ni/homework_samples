# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9

# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11

# Раскомментируйте нужную строку

print('*'*7, 'Поместиться ли лист в конверт?'.upper(), '*'*7)
print('Размер конверта:', envelop_x, 'на', envelop_y)
print('Размер листа:', paper_x, 'на', paper_y)

# Решение 1
# if paper_x <= envelop_x:
#     if paper_y <= envelop_y:
#         print('ДА!')
#     else: 
#         print('НЕТ!')
# else:
#     print('НЕТ!')

# Решение 2
if paper_x <= 0 or paper_y <= 0:
    print('Размер листа не может быть меньше 0!')
elif paper_x > envelop_x:
    print('НЕТ!')
elif paper_y > envelop_y:
    print('НЕТ!')
else:
    print('ДА!')
