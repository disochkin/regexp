import re
# result = re.match(r'\d', '+7 (495) 983-36-99 доб. 2926')
# print (result)

born = "+7 (495) 983-36-99 доб. 2926"

# Удалим комментарий из строки
dob = re.sub(r'\D', "", born)
print("Дата рождения:", dob)
print("Дата рождения:", dob[11:])
