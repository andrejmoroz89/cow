# Базовые операции со строками.
# Найти самое длинное слово в введенном предложении

TEXT = input()
NEW_TEXT = TEXT.split(" ")
BIGGEST = str()
for i in NEW_TEXT:
    if len(i) > len(BIGGEST):
        BIGGEST = i
print(BIGGEST)
print(len(BIGGEST))
