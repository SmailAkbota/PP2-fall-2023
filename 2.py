# /a = []
# for i in range(int(input())):
#     a.append(int(input()))
# print(a)
# # дано: s = 'ab12c59p7dq'
# надо: извлечь цифры в список digits,
# чтобы стало так:
# digits == [1, 2, 5, 9, 7]
# s = input()  # s == '1 2 3'
# a = s.split()  # a == ['1', '2', '3']
# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)

# # Перебор элементов списка и вывод четных индексов и их соответствующих значений
# for index in range(len(a)):
#     if index % 2 == 0:
#         print(f"Индекс: {index}, Значение: {a[index]}")
s = input()
a = s.split()
for i in range(0,len(a)):
    a[i] = int(a[i])
    if a[i] % 2 == 0:
        print(a[i])
    