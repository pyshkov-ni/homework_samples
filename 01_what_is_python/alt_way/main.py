# Допустим, у нас есть база данных с телефонными номерами.
# Номера телефонов перемешаны с ненужными символами.
# Так что дальнейшая обработка затруднена.
# Вот программа, если номера телефонов находятся в excel файле.

# Для работы с .xlsx нам нужны функции из библиотеки pandas
# Подключимся к библиотеке pandas
import pandas as pd
import mymodule as m  # импортируем содержимое файла mymodule
from pprint import pprint # модуль позвляет использовать красивый вывод на экран

print('========= СКРИПТ ДЛЯ ОЧИСТКИ НОМЕРОВ ТЕЛЕФОНОВ ОТ НЕНУЖНЫХ СИМВОЛОВ =========')

# Укажем путь к файлу в виде перемнной со строкой
######## ВНИМАНИЕ!!! Укажите тот путь, где будет находится ваш файл!!! ########
PATH = input(
    'Введите путь к файлу формата .xlsx\nПуть запишите в формате /Users/User/file.xlsx :'
    )
NEWFILE_PATH = input(
    '\nДля сохранения введите путь и название файла в формате .xlsx\nПуть запишите в формате /Users/User/new_file.xlsx :'
    )

# Используем метод из pandas, чтобы выгрузить .xlsx. Получим тип данных таблица
excel_df = pd.read_excel(PATH, sheet_name='Worksheet')
# Превратим таблицу в список
phone_list = excel_df['phone_number'].values.tolist()
clean_phone_list = m.phone_list_cleaner(phone_list)

print('\n', '*'*77, '\nВот ваш результат:\n')
pprint(clean_phone_list)

# Обработанный список переводим в таблицу с помощью pandas
new_df = pd.DataFrame(clean_phone_list, columns =['phones'])
# Таблицу сохраняем в новый файл .xlsx
new_df.to_excel(NEWFILE_PATH, sheet_name='clean_numbers', index=False)

print('\nПроверьте результат по указнной директории\nСпасибо вам за использование скрипта!')
