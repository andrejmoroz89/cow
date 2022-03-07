STROKA = input(str())
NEW_STRING = STROKA.replace(' ', '')
STRING = NEW_STRING[::-1]
print(NEW_STRING)
print(STRING)
if NEW_STRING == STRING:
    print(' палиндром')
else:
    print(' не палиндром')
