######## ВНИМАНИЕ!!! скрипт составлен для ресурса replit.com!!! ########
# Допустим, у нас есть база данных с телефонными номерами.
# Номера телефонов перемешаны с ненужными символами.
# Так что дальнейшая обработка затруднена.
# Вот программа, если номера телефонов находятся в excel файле.

# Для работы с .xlsx нам нужны функции из библиотеки pandas
# Подключимся к библиотеке pandas
import pandas as pd
import sys  # подключимся к библиотеке sys

# используем метод из sys для вывода информации из пути
sys.path.insert(0, '/home/runner/pythonforranepa/')
import mymodule as m  # импортируем содержимое файла mymodule

# Укажем путь к файлу в виде перемнной со строкой
######## ВНИМАНИЕ!!! Укажите тот путь, где будет находится ваш файл!!! ########
PATH = '/home/runner/pythonforranepa/phone_numbers.xlsx'
NEWFILE_PATH = '/home/runner/pythonforranepa/clean_phone_numbers.csv'

# Используем метод из pandas, чтобы выгрузить .xlsx. Получим тип данных таблица
excel_df = pd.read_excel(PATH, sheet_name='Worksheet')

# Превратим таблицу в список
phone_list = excel_df['phone_number'].values.tolist()
clean_phone_list = m.phone_list_cleaner(phone_list)

print(clean_phone_list)

# Обработанный список переводим в таблицу с помощью pandas
new_df = pd.DataFrame(clean_phone_list, columns =['phones'])
# Таблицу сохраняем в новый файл .xlsx
new_df.to_csv(NEWFILE_PATH, index=False)
