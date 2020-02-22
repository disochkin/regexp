import re
# "слияние" списков
def merge_lists(list1, list2):
    result = ["", "", "", "", "", "", ""]
    for k in range(len(list2)):
        if list2[k] != "":
            result[k] = list2[k]
        else:
            result[k] = list1[k]
    return result

# исправление формата телефонного номера к виду +7(999)999-99-99 доб.9999;
def fix_number_format(number):
    number = re.sub(r"^[\7|8]", "+7", number)
    digit = []
    additional_digit = " доб."
    for j in re.finditer(r"\d", number):
        digit.append(j.group())
    result = (
        f'+{digit[0]}({digit[1]}{digit[2]}{digit[3]}){digit[4]}{digit[5]}{digit[5]}-{digit[6]}{digit[6]}-{digit[8]}{digit[9]}')
    for j in range(len(digit)):
        if j > 10:
            additional_digit = additional_digit + f'{digit[j]}'
    if len(additional_digit) > 5:
        result = result + additional_digit
    return result


from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)

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
    extended_dict[contacts_list[i][0] + " " + contacts_list[i][1]] = \
        merge_lists(extended_dict.get(contacts_list[i][0] + " " + contacts_list[i][1], ["", "", "", "", "", "", ""]),
                    contacts_list[i])

# приводим телефонный номер к формату +7(999)999-99-99 доб.9999;
for i in range(len(extended_dict.values())):
    if i > 1:
        #print(extended_dict.values)

        extended_dict.values()[i][5] = fix_number_format(extended_dict.values()[i][5])
    #print(item[6])



# исправление формата телефонного номера


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
