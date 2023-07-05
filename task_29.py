# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

#1
# n = int(input('Введите число: '))
# max = n
# while n != 0:
#     n = int(input('Введите число: '))
#     if n > max:
#         max = n
# print('Максимальное число', max)

#2
# max = 0
# n = -1
# while n != 0:
# n = int(input("Введите число: "))
# if n > max:
# max = n
# print("Максимальное число: ", max)

#3
max = 0
while n := int(input('Введите число: ')):
    if n > max:
        max = n
print('Максимальное число', max)