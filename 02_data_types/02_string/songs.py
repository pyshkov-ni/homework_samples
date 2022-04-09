# Есть строка с перечислением песен
my_favorite_songs = 'Waste a Moment, New Salvation, Staying\' Alive, Out of Touch, A Sorta Fairytale'

# Выведите на консоль с помощью индексации, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])

# Решение с помощью индекции строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('A') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('N') : 
     my_favorite_songs.find(', S')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('O') : my_favorite_songs.rfind(',')
    ]

print(first_song, last_song, second_song, previous_song)
