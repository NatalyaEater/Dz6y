# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# print('Введите число')
# str = input()
# num = int(str.strip('0,'))

# sum = 0
# while num > 0:
#     sum = sum+(num % 10)
#     num = num // 10

# print('Сумма цифр числа',str  ,'равна:' , sum)

num=list(map(int,input().strip('0,')))
x=0
for i in num:
    x=x+i
print(x)