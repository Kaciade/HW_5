# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.


list_1 = list(str(input("Введите строку: ")))
list_2 = list()


for i in range(len(list_1)-1):
    if list_1.count(list_1[i]) > 1:
        m = list_1[i]+str(list_1.count(list_1[i]))
        list_2.append(m)
    else:
        list_2.append(list_1[i])

print(list_2)
