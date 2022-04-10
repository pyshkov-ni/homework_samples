# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 3, 6

# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6

# Раскомментируйте нужную строку

print('*'*7, 'Войдет ли кирпич в отверстие?'.upper(), '*'*7)
print('Размер отверстия:', hole_x, 'на', hole_y)
print('Размер кирпича:', brick_x, 'на', brick_y)

if brick_x <= 0 or brick_y <= 0:
    print('Размер кирпича не может быть меньше 0!')
elif brick_x > hole_x:
    print('НЕ ПРОХОДИТ')
elif brick_y > hole_y:
    print('НЕ ПРОХОДИТ')
else:
    print('ПРОХОДИТ')
