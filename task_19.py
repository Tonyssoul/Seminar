# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

k = int(input('Введите на какое число элементов нужен сдвиг: '))
lst = [i for i in range(1, 10)]
print(lst)

for i in range(k):
    lst.insert(0, lst.pop())
print(lst)

#второе решение
print(lst[-k:] + lst[:-k])