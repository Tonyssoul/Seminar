# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

import random
n = int(input('Введите колличество оценок:'))
lst = [random.randint(1, 5) for i in range(n)]
print(lst)
max_mark = max(lst)
min_mark = min(lst)

for i in range(n):
    if lst[i] == max_mark:
        lst[i] = min_mark

print(lst)