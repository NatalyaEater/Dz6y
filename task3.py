# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# print('Введите десятичное число')
# a = int(input())
# print()

# def machine(num):
#     code=''
#     while num > 0:
#         code = str(num%2) + code
#         num //=2
#     print('Преобразованное десятичное число будет иметь вид:',code)

# machine(a)

machine = lambda x: format(x, 'b')
print(machine(int(input())))