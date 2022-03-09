# Базовые операции со строками.
# Вводится строка. Удалить из нее все пробелы, после этого определить, является ли она палиндромом, т.е.
# одинаково пишется как с начала так и с конца.

STROKA = input(str())
NEW_STRING = STROKA.replace(' ', '')
STRING = NEW_STRING[::-1]
print(NEW_STRING)
print(STRING)
if NEW_STRING == STRING:
    print(' палиндром')
else:
    print(' не палиндром')
