# def merge_lists(list1,list2):
#     result = list()
#     for i in range(len(list2)):
#         if list2[i] != "":
#             result.append(list2[i])
#         else:
#             result.append(list1[i])
#     return result
#
#
# list1 = ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', '', '+74959130037', '']
# list2 = ['Мартиняхин', 'Виталий', 'Геннадьевич', 'ФНС', 'cоветник отдела Интернет проектов Управления информационных технологий', '', '']
import re
tel = ["+7 (495) 913-04-78", "+74959130037","8 495-913-0168","+7 (495) 983-36-99 доб. 2926","8(495)748-49-73","+7 (495) 913-11-11 (доб. 0792)"]

for i in range(len(tel)):
    tel[i] = re.sub(r"^[\7|8]", "+7", tel[i])
    digit =[]
    additional_digit = " доб."
    for j in re.finditer(r"\d", tel[i]):
        digit.append(j.group())
    result = (f'+{digit[0]}({digit[1]}{digit[2]}{digit[3]}){digit[4]}{digit[5]}{digit[5]}-{digit[6]}{digit[6]}-{digit[8]}{digit[9]}')
    for j in range(len(digit)):
        if j > 10:
            additional_digit = additional_digit + f'{digit[j]}'

    if len(additional_digit) > 5:
        result = result + additional_digit

    print(result)


