# Допустим, у нас есть база данных с телефонными номерами.
# Номера телефонов перемешаны с ненужными символами.
# Так что дальнейшая обработка затруднена.
# Вот программа, если номера телефонов находятся в excel файле.

# Для работы с .xlsx нам нужны функции из библиотеки pandas
# Подключимся к библиотеке pandas
import pandas as pd

# Укажем путь к файлу в виде перемнной со строкой
######## ВНИМАНИЕ!!! Укажите тот путь, где будет находится ваш файл!!! ########

PATH = '/Users/nikita/edu_projects/homework_samples/01_what_is_python/phone_numbers.xlsx'
NEWFILE_PATH = '/Users/nikita/edu_projects/homework_samples/01_what_is_python/clean_phone_numbers.xlsx'

# Представим в виде функции программу char_cleaner_for_str
# Добавили перевод перменной в строку!!!


def char_clean(s):
    s = str(s)  # нужна строка, так как нельзя индексировать число
    new_s = ''  # создадим новую пустую строку
    for i in s:
        if i.isdigit() is True:  # является ли символ цифрой
            new_s += i  # Добавить символ в строку
        else:
            pass  # пропустить символ
    return new_s  # вернуть из функции обработанное значение


# Используем метод из pandas, чтобы выгрузить .xlsx. Получим тип данных таблица
excel_df = pd.read_excel(PATH, sheet_name='Worksheet')

# Превратим таблицу в список
phone_list = excel_df['phone_number'].values.tolist()
clean_phone_list = []  # создаем пустой список для очищенных телефонов
phone = ''  # вот пременная номер телефона строка

# Тело цикла для обработки каждого элемента по индексу в списке
for i in range(len(phone_list)):
    phone = phone_list[i]  # выбираем элемент списка по индексу i
    new_phone = char_clean(phone)  # обрабатываем телефон по функции выше
    clean_phone_list.append(new_phone)  # добавляем номер телефона в список

# Обработанный список переводим в таблицу с помощью pandas
new_df = pd.DataFrame(clean_phone_list)
# Таблицу сохраняем в новый файл .xlsx
new_df.to_excel(NEWFILE_PATH, sheet_name='clean_numbers', index=False)
