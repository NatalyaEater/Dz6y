# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример: Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

# print('Введите число')
# num = int(input())

# print ('Сумма чисел последовательности (1+1/n)**n будет равна:')
# for i in range(1, num+1):
#     composition = round((1+1/i)**i, 0) 
#     print(composition, end=" ")

num = int(input())
composition = lambda i: round((1+1/i)**i, 0)
res = [(i, composition(i)) for i in range(1, num+1)]
print(res)