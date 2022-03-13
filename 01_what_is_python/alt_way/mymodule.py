# Модуль хранит функции, которые мы будем использовать в других файлах
# Подробнее о функциях в файлах char_cleaner_for_list

def char_clean(s):
    s = str(s)
    new_s = str()
    
    for i in s:
        if i.isdigit() is True:
            new_s = new_s + i
        else:
            pass
    return new_s


def phone_list_cleaner(phone_list):
    clean_phone_list = list()
    phone = ''

    for i in range(len(phone_list)):
        phone = phone_list[i] 
        new_phone = char_clean(phone)
        clean_phone_list.append(new_phone)
    return clean_phone_list