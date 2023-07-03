# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза

import random

n = int(input('Введите колличество арбузов:'))
weightmax, minweight  = 0, 20
for _ in range(n):
    a = random.randint(1, 20)
    print(a, end=' ')
    if a > weightmax:
        weightmax = a
    elif a < minweight:
        minweight = a
    


print('\n', f"Вес максимального арбуза {weightmax}, а вес минимального арбуза {minweight}")