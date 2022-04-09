# Задача 1
# Дан радиус круга radius = 16
# Выведите на консоль значение площади данного круга
# Формула площади круга pi * radius ** 2
# радиус radius = 16
# число пи pi = 3.1415926 
# Выведите ответ с точностью до 4-х знаков после запятой
# Точность указывается в функции round()

radius = 16
pi = 3.1415926

square_cycle = pi * radius ** 2
square_cycle_round = round(square_cycle, 4)

print(square_cycle_round)
