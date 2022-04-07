# Вводится дата в формате dd.mm.yyyy Вывести дату в формате mm\dd\yyyy

DATA = input('введите дату в формате dd.mm.yyyy\n')
print(DATA[3:6] + DATA[0:3] + DATA[6:10])
