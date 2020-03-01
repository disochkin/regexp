import re
# "слияние" списков


def merge_lists(list1, list2):
    result = []
    for k in range(len(list2)):
        if list2[k] != "":
            result.append(list2[k])
        else:
            result.append(list1[k])
    return result


def get_empty_list(count):
    result = []
    for item in range(count):
        result.append("")
    return result


# исправление формата телефонного номера к виду +7(999)999-99-99 доб.9999;
def fix_number_format(number):
    number = re.sub(r"^[\7|8]", "7", number)
    digits = re.sub(r'\D', "", number)
    result = "+{}({}{}{}){}{}{}-{}{}-{}{}".format(*digits)
    if digits[11:]:
        result = result + " доб." + digits[11:]
    return result

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# упорядочивание расположения ФИО по колонкам
for item_contact_list in contacts_list:
    fullname = (item_contact_list[0] + " " + item_contact_list[1] + " " + item_contact_list[2]).rstrip()
    fullname_list = fullname.split(" ")
    for i in range(len(fullname_list)):
        item_contact_list[i] = fullname_list[i]

# удаление "дубликатов"
extended_dict = {}
i = 0
for i in range(len(contacts_list)):
    key_name = contacts_list[i][0] + " " + contacts_list[i][1]
    extended_dict[key_name] = merge_lists(extended_dict.get(key_name, get_empty_list(len(contacts_list[0]))), contacts_list[i])

#словарь приводим к списку
contacts_list.clear()
for key in extended_dict.keys():
    contacts_list.append(extended_dict[key])

# приводим телефонный номер к формату +7(999)999-99-99 доб.9999;
for i in range(len(contacts_list)):
    if i > 0:
        contacts_list[i][5] = fix_number_format(contacts_list[i][5])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
     datawriter = csv.writer(f, delimiter=',')
     # Вместо contacts_list подставьте свой список
     datawriter.writerows(contacts_list)
