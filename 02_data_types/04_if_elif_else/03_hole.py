# Заданы размеры прямоугольного отверстия hole_x, hole_y и размеры кубика с гранью cube_х
# Пройдет ли кубик через прямоугольное отверстие?

hole_x, hole_y = 8, 9
cube_x = 11

# cube_x = 6
# cube_x = 3
# cube_x = 10
# cube_x = 5
# cube_x = 9
# cube_x = 8

# Раскомментируйте нужную строку

print('*'*7, 'Войдет ли кубик в отверстие?'.upper(), '*'*7)
print('Размер отверстия:', hole_x, 'на', hole_y)
print('Грань кубика:', cube_x)

# Решение 1
if hole_x < cube_x:
    print('НЕ ПРОХОДИТ')
elif hole_y < cube_x:
    print('НЕ ПРОХОДИТ')
else:
    print('ПРОХОДИТ')

# Решение 2
if hole_x < cube_x or hole_y < cube_x:
    print('НЕ ПРОХОДИТ')
else:
    print('ПРОХОДИТ')
