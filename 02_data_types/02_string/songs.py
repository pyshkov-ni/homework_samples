# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, New Salvation, Staying\' Alive, Out of Touch, A Sorta Fairytale'

# Выведите на консоль с помощью индексации, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])